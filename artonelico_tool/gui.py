from __future__ import annotations

import sqlite3
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

from .patcher import build_iso
from .project import (
    backup_project, connect, create_from_iso, encoded_size, ensure_source_identity, mark_reviewed,
    planned_iso_counts, project_stats, save_text, select_final_text,
)
from .quality import ensure_default_glossary
from .reports import export_project_reports, import_project_csv
from .translator import TranslationConfig, run_queue


class MainWindow(tk.Tk):
    def __init__(self, initial_project: Path | None = None):
        super().__init__()
        self.title("Ar tonelico PT-BR Studio")
        self.geometry("1500x850")
        self.minsize(1050, 650)
        self.project_path: Path | None = None
        self.db: sqlite3.Connection | None = None
        self.current_id: int | None = None
        self.translation_config: TranslationConfig | None = None
        self.glossary_path = ""
        self.stop_requested = False
        self.busy = False
        self._autosave_job = None
        self._loading_line = False
        self._build_ui()
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        if initial_project and initial_project.exists():
            self.open_project(initial_project)

    def _build_ui(self):
        toolbar = ttk.Frame(self, padding=6)
        toolbar.pack(fill="x")
        ttk.Button(toolbar, text="Nova a partir da ISO", command=self.new_project).pack(side="left", padx=2)
        ttk.Button(toolbar, text="Abrir projeto", command=self.choose_project).pack(side="left", padx=2)
        ttk.Button(toolbar, text="Configurar Azure/DeepL", command=self.configure_api).pack(side="left", padx=14)
        ttk.Button(toolbar, text="Traduzir pendentes", command=self.start_translation).pack(side="left", padx=2)
        ttk.Button(toolbar, text="Parar", command=lambda: setattr(self, "stop_requested", True)).pack(side="left", padx=2)
        ttk.Button(toolbar, text="Exportar CSV/relatórios", command=self.export_reports).pack(side="right", padx=8)
        ttk.Button(toolbar, text="Importar CSV", command=self.import_csv).pack(side="right", padx=2)
        ttk.Button(toolbar, text="Gerar ISO (revisados + automáticos)", command=self.generate_iso).pack(side="right", padx=2)

        filters = ttk.Frame(self, padding=(6, 0, 6, 6))
        filters.pack(fill="x")
        ttk.Label(filters, text="Buscar:").pack(side="left")
        self.search = tk.StringVar()
        entry = ttk.Entry(filters, textvariable=self.search, width=45)
        entry.pack(side="left", padx=5)
        entry.bind("<Return>", lambda _: self.refresh())
        self.filter = tk.StringVar(value="Todos")
        ttk.Combobox(filters, textvariable=self.filter, state="readonly", width=19,
                     values=("Todos", "Pendentes", "Tamanho certo", "Acima dos bytes", "Com erro",
                             "Revisados aprovados", "Revisão pendente", "Protegidos")).pack(side="left", padx=5)
        ttk.Button(filters, text="Aplicar", command=self.refresh).pack(side="left")
        self.summary = ttk.Label(filters, text="Nenhum projeto aberto")
        self.summary.pack(side="right")

        content = ttk.Frame(self)
        content.pack(fill="both", expand=True, padx=6, pady=(0, 6))
        pane = ttk.Panedwindow(content, orient="vertical")
        pane.pack(side="left", fill="both", expand=True)
        table_frame = ttk.Frame(pane)
        pane.add(table_frame, weight=3)
        columns = ("ref", "original", "automatic", "translation", "size", "reviewed", "review_state")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
        labels = {"ref":"Arquivo / ID", "original":"Texto original em inglês",
                  "automatic":"Base automática/localizada", "translation":"Tradução em edição",
                  "size":"Tamanho", "reviewed":"Texto final revisado", "review_state":"Revisão"}
        widths = {"ref":150, "original":360, "automatic":330, "translation":330,
                  "size":100, "reviewed":330, "review_state":110}
        for col in columns:
            self.tree.heading(col, text=labels[col])
            self.tree.column(col, width=widths[col], minwidth=70, stretch=col not in ("ref", "size"))
        yscroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        xscroll = ttk.Scrollbar(table_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
        self.tree.tag_configure("valid", background="#eaf8ec")
        self.tree.tag_configure("oversized", background="#fff3d6")
        self.tree.tag_configure("error", background="#ffe4e4")
        self.tree.tag_configure("protected", foreground="#777777")
        self.tree.grid(row=0, column=0, sticky="nsew")
        yscroll.grid(row=0, column=1, sticky="ns")
        xscroll.grid(row=1, column=0, sticky="ew")
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)
        self.tree.bind("<<TreeviewSelect>>", self.load_selected)

        editor = ttk.Frame(pane, padding=6)
        pane.add(editor, weight=1)
        editor.columnconfigure(1, weight=1)
        labels = (
            "Japonês original",
            "Inglês de referência",
            "Base automática/localizada",
            "Tradução em edição",
            "Texto final revisado",
            "Contexto: falas próximas",
        )
        for row, label in enumerate(labels):
            ttk.Label(editor, text=label).grid(row=row, column=0, sticky="nw", padx=(0, 8), pady=3)
        self.original_jp_text = tk.Text(editor, height=2, wrap="word", state="disabled", bg="#faf8f5")
        self.original_text = tk.Text(editor, height=2, wrap="word", state="disabled")
        self.automatic_text = tk.Text(editor, height=2, wrap="word", state="disabled")
        self.translation_text = tk.Text(editor, height=3, wrap="word")
        self.reviewed_text = tk.Text(editor, height=3, wrap="word")
        self.context_text = tk.Text(editor, height=3, wrap="word", state="disabled", bg="#f4f4f4")
        for row, widget in enumerate((self.original_jp_text, self.original_text, self.automatic_text,
                                      self.translation_text, self.reviewed_text, self.context_text)):
            widget.grid(row=row, column=1, sticky="nsew", pady=3)
        self.translation_text.bind("<KeyRelease>", self._edited_line)
        self.reviewed_text.bind("<KeyRelease>", self._edited_line)
        actions = ttk.Frame(editor)
        actions.grid(row=6, column=1, sticky="ew", pady=4)
        ttk.Button(actions, text="Salvar linha", command=self.save_current).pack(side="left")
        ttk.Button(actions, text="Copiar tradução para texto final", command=self.copy_translation).pack(side="left", padx=6)
        ttk.Button(actions, text="Marcar como revisado", command=self.approve_current).pack(side="left", padx=(0, 6))
        ttk.Button(actions, text="Limpar texto final", command=self.clear_reviewed).pack(side="left")
        self.line_status = ttk.Label(actions, text="")
        self.line_status.pack(side="right")
        self._build_progress_panel(content)
        self.status = tk.StringVar(value="Pronto")
        ttk.Label(self, textvariable=self.status, relief="sunken", anchor="w", padding=4).pack(fill="x", side="bottom")

    def _build_progress_panel(self, parent):
        colors = {
            "background": "#10263d", "muted": "#9fc0d4", "title": "#ffd35a",
            "correct": "#23e58b", "error": "#ff4e78", "pending": "#79d2ff",
            "oversized": "#ffbd59", "protected": "#b8a7e8", "track": "#263d53",
        }
        panel = tk.Frame(parent, width=235, bg=colors["background"], padx=12, pady=12)
        panel.pack(side="right", fill="y", padx=(7, 0))
        panel.pack_propagate(False)
        tk.Label(panel, text="PROGRESSO", bg=colors["background"], fg=colors["title"],
                 font=("Segoe UI", 10, "bold"), anchor="w").pack(fill="x")
        self.review_progress_text = tk.StringVar(value="0 revisados / 0  •  0%")
        tk.Label(panel, textvariable=self.review_progress_text, bg=colors["background"], fg=colors["muted"],
                 font=("Segoe UI", 9), anchor="w", pady=9).pack(fill="x")
        self.review_progress = tk.Canvas(panel, height=16, bg=colors["track"], bd=0,
                                         highlightthickness=1, highlightbackground="#8ba0b3")
        self.review_progress.pack(fill="x")
        self.review_progress.create_rectangle(0, 0, 0, 16, fill=colors["title"], outline="", tags="bar")
        self.review_progress.bind("<Configure>", lambda _event: self._draw_review_progress())
        self._review_fraction = 0.0

        self.translation_progress_text = tk.StringVar(value="0 traduzidos")
        tk.Label(panel, textvariable=self.translation_progress_text, bg=colors["background"], fg=colors["muted"],
                 font=("Segoe UI", 8), anchor="w", pady=7).pack(fill="x")
        tk.Frame(panel, height=1, bg="#38516a").pack(fill="x", pady=(2, 9))

        self.progress_counts = {}
        for key, label, color in (
            ("correct", "Corretos", colors["correct"]),
            ("errors", "Com erro", colors["error"]),
            ("pending", "Pendentes", colors["pending"]),
            ("review_drafts", "Revisão pendente", colors["title"]),
            ("oversized", "Acima dos bytes", colors["oversized"]),
            ("protected", "Protegidos", colors["protected"]),
        ):
            row = tk.Frame(panel, bg=colors["background"])
            row.pack(fill="x", pady=3)
            tk.Label(row, text=label, bg=colors["background"], fg=colors["muted"],
                     font=("Segoe UI", 9), anchor="w").pack(side="left")
            variable = tk.StringVar(value="0")
            tk.Label(row, textvariable=variable, bg=colors["background"], fg=color,
                     font=("Segoe UI", 9, "bold"), anchor="e").pack(side="right")
            self.progress_counts[key] = variable

        tk.Frame(panel, height=1, bg="#38516a").pack(fill="x", pady=(10, 7))
        self.visible_count = tk.StringVar(value="Nenhum projeto aberto")
        tk.Label(panel, textvariable=self.visible_count, bg=colors["background"], fg=colors["muted"],
                 font=("Segoe UI", 8), anchor="w", justify="left", wraplength=205).pack(fill="x")

    def _draw_review_progress(self):
        width = max(0, self.review_progress.winfo_width() - 2)
        self.review_progress.coords("bar", 1, 1, 1 + round(width * self._review_fraction), 15)

    def _refresh_progress_panel(self, visible: int | None = None):
        if not self.db:
            return
        stats = project_stats(self.db)
        eligible = stats["eligible"]
        reviewed = stats["reviewed"]
        percent = round(reviewed * 100 / eligible) if eligible else 0
        self._review_fraction = reviewed / eligible if eligible else 0.0
        self.review_progress_text.set(f"{reviewed} revisados / {eligible}  •  {percent}%")
        self.translation_progress_text.set(f"{stats['translated']} traduzidos de {eligible}")
        for key, variable in self.progress_counts.items():
            variable.set(str(stats[key]))
        if visible is not None:
            shown = min(visible, 5000)
            suffix = " (limite: 5000)" if visible > 5000 else ""
            self.visible_count.set(f"Exibindo {shown} de {visible}{suffix}\nTotal no projeto: {stats['total']}")
        self._draw_review_progress()

    def _update_line_preview(self, _event=None):
        if not self.db or self.current_id is None:
            return
        row = self.db.execute("SELECT * FROM dialogues WHERE id=?", (self.current_id,)).fetchone()
        reviewed = self.reviewed_text.get("1.0", "end-1c")
        translation = self.translation_text.get("1.0", "end-1c")
        size = encoded_size(reviewed or translation) if (reviewed or translation) else 0
        preview_row = dict(row)
        if reviewed != row["reviewed"]:
            preview_row["reviewed"] = reviewed
            preview_row["review_status"] = "draft"
        _, iso_source = select_final_text(preview_row)
        iso_label = {"reviewed": "REVISADO", "automatic": "AUTOMÁTICO", "original": "ORIGINAL"}[iso_source]
        if size is None:
            self.line_status.config(
                text=f"Edição: caractere não suportado  •  ISO: {iso_label}",
                foreground="#d52b55",
            )
        else:
            fits = not size or size <= row["original_bytes"]
            approved = (
                reviewed.strip() and reviewed == row["reviewed"]
                and row["review_status"] == "approved"
            )
            review_note = "  •  APROVADO" if approved else "  •  REVISÃO PENDENTE" if reviewed.strip() else ""
            self.line_status.config(
                text=f"{size}/{row['original_bytes']} bytes  •  {'CERTO' if fits else 'ACIMA'}"
                     f"{review_note}  •  ISO: {iso_label}",
                foreground="#168653" if fits else "#b56a00",
            )

    def _edited_line(self, _event=None):
        if self._loading_line:
            return
        self._update_line_preview()
        if self._autosave_job is not None:
            self.after_cancel(self._autosave_job)
        self._autosave_job = self.after(900, self._autosave_current)

    def _autosave_current(self):
        self._autosave_job = None
        if not self.db or self.current_id is None:
            return
        save_text(
            self.db, self.current_id,
            self.translation_text.get("1.0", "end-1c"),
            self.reviewed_text.get("1.0", "end-1c"),
        )
        self.status.set("Alterações salvas automaticamente; texto final editado exige nova aprovação")
        self._refresh_progress_panel()

    def _background(self, function, done=None):
        if self.busy:
            messagebox.showinfo("Operação em andamento", "Aguarde ou clique em Parar.")
            return
        self.busy = True
        def worker():
            try:
                result = function()
                self.after(0, lambda: self._finish_background(result, done))
            except Exception as exc:
                self.after(0, lambda error=exc: self._fail_background(error))
        threading.Thread(target=worker, daemon=True).start()

    def _finish_background(self, result, done=None):
        self.busy = False
        if done:
            done(result)

    def _fail_background(self, error: Exception):
        self.busy = False
        self.status.set("Falha")
        messagebox.showerror("Erro", str(error))

    def new_project(self):
        iso = filedialog.askopenfilename(title="Selecione a ISO original", filetypes=(("Imagem ISO", "*.iso"),))
        if not iso: return
        project = filedialog.asksaveasfilename(title="Salvar projeto", defaultextension=".atproj",
                                               filetypes=(("Projeto Ar tonelico", "*.atproj"),))
        if not project: return
        self.status.set("Extraindo 976 arquivos de diálogo...")
        def progress(done, total, name):
            if done % 20 == 0: self.after(0, lambda: self.status.set(f"Extraindo {done}/{total}: {name}"))
        self._background(lambda: create_from_iso(Path(iso), Path(project), progress),
                         lambda count: (self.open_project(Path(project)), self.status.set(f"Concluído: {count} entradas")))

    def choose_project(self):
        path = filedialog.askopenfilename(filetypes=(("Projeto Ar tonelico", "*.atproj"), ("Todos", "*.*")))
        if path: self.open_project(Path(path))

    def open_project(self, path: Path):
        if self.db: self.db.close()
        self.project_path = path
        self.db = connect(path)
        ensure_source_identity(self.db)
        self.glossary_path = str(ensure_default_glossary(path))
        self.title(f"Ar tonelico PT-BR Studio — {path.name}")
        self.refresh()

    def refresh(self):
        if not self.db: return
        where, params = [], []
        query = self.search.get().strip()
        if query:
            # OCR/copied screenshots frequently contain visual line breaks.
            # Search each word independently and across every text column. A
            # direct search also ignores the status filter so an existing row
            # cannot be hidden merely because it belongs to another category.
            cols = {col[1] for col in self.db.execute("PRAGMA table_info(dialogues)")}
            has_jp = "original_jp" in cols
            for token in query.split():
                if has_jp:
                    where.append(
                        "(original LIKE ? OR automatic LIKE ? OR translation LIKE ? "
                        "OR reviewed LIKE ? OR event_file LIKE ? OR original_jp LIKE ?)"
                    )
                    params.extend([f"%{token}%"] * 6)
                else:
                    where.append(
                        "(original LIKE ? OR automatic LIKE ? OR translation LIKE ? "
                        "OR reviewed LIKE ? OR event_file LIKE ?)"
                    )
                    params.extend([f"%{token}%"] * 5)
        selected = self.filter.get()
        if query:
            selected = "Todos"
        if selected == "Pendentes":
            where.append("length(trim(automatic))=0 AND length(trim(translation))=0 "
                         "AND length(trim(reviewed))=0 AND locked=0")
        elif selected == "Tamanho certo":
            where.append("locked=0 AND size_ok=1 AND error='' AND (length(trim(automatic))>0 OR length(trim(translation))>0 OR length(trim(reviewed))>0)")
        elif selected == "Acima dos bytes":
            where.append("locked=0 AND size_ok=0 AND error='' AND (length(trim(automatic))>0 OR length(trim(translation))>0 OR length(trim(reviewed))>0)")
        elif selected == "Com erro":
            where.append("locked=0 AND error<>'' AND (length(trim(automatic))>0 OR length(trim(translation))>0 OR length(trim(reviewed))>0)")
        elif selected == "Revisados aprovados":
            where.append("length(trim(reviewed))>0 AND review_status='approved'")
        elif selected == "Revisão pendente":
            where.append("length(trim(reviewed))>0 AND review_status<>'approved'")
        elif selected == "Protegidos": where.append("locked=1")
        clause = " WHERE " + " AND ".join(where) if where else ""
        visible = self.db.execute("SELECT COUNT(*) FROM dialogues" + clause, params).fetchone()[0]
        sql = "SELECT * FROM dialogues" + clause + " ORDER BY id LIMIT 5000"
        self.tree.delete(*self.tree.get_children())
        for row in self.db.execute(sql, params):
            has_text = bool(row["automatic"].strip() or row["translation"].strip() or row["reviewed"].strip())
            if row["locked"]:
                status = "PROTEGIDO"
            elif not has_text:
                status = "PENDENTE"
            else:
                if row["error"]:
                    status = "ERRO"
                elif not row["size_ok"]:
                    status = "ACIMA"
                else:
                    status = "CERTO"
                status += f" {row['translated_bytes']}/{row['original_bytes']} B"
            tag = "protected" if row["locked"] else "error" if row["error"] else "oversized" if not row["size_ok"] and has_text else "valid" if has_text else ""
            self.tree.insert("", "end", iid=str(row["id"]), tags=(tag,) if tag else (), values=(
                f"{Path(row['event_file']).name}:{row['entry_index']}", row["original"], row["automatic"],
                row["translation"], status, row["reviewed"],
                "APROVADO" if row["review_status"] == "approved" else "PENDENTE" if row["reviewed"].strip() else "—"))
        stats = project_stats(self.db)
        self.summary.config(
            text=f"Traduzidos {stats['translated']}  |  aprovados {stats['reviewed']}  |  revisão pendente {stats['review_drafts']}  |  acima {stats['oversized']}  |  erros {stats['errors']}"
        )
        self._refresh_progress_panel(visible)

    def load_selected(self, _event=None):
        selection = self.tree.selection()
        if not selection or not self.db: return
        selected_id = int(selection[0])
        if self.current_id is not None and self.current_id != selected_id and not self._loading_line:
            if self._autosave_job is not None:
                self.after_cancel(self._autosave_job)
                self._autosave_job = None
            save_text(
                self.db, self.current_id,
                self.translation_text.get("1.0", "end-1c"),
                self.reviewed_text.get("1.0", "end-1c"),
            )
        self.current_id = selected_id
        row = self.db.execute("SELECT * FROM dialogues WHERE id=?", (self.current_id,)).fetchone()
        self._loading_line = True
        for widget in (self.original_jp_text, self.original_text, self.automatic_text,
                       self.translation_text, self.reviewed_text, self.context_text):
            widget.config(state="normal"); widget.delete("1.0", "end")
        orig_jp = row["original_jp"] if "original_jp" in row.keys() and row["original_jp"] else ""
        self.original_jp_text.insert("1.0", orig_jp); self.original_jp_text.config(state="disabled")
        self.original_text.insert("1.0", row["original"]); self.original_text.config(state="disabled")
        self.automatic_text.insert("1.0", row["automatic"]); self.automatic_text.config(state="disabled")
        self.translation_text.insert("1.0", row["translation"])
        self.reviewed_text.insert("1.0", row["reviewed"])
        nearby = self.db.execute(
            "SELECT entry_index,speaker_id,original,translation,reviewed FROM dialogues "
            "WHERE event_file=? AND entry_index BETWEEN ? AND ? ORDER BY entry_index",
            (row["event_file"], max(0, row["entry_index"] - 2), row["entry_index"] + 2),
        ).fetchall()
        context = []
        for item in nearby:
            marker = ">" if item["entry_index"] == row["entry_index"] else " "
            current = item["reviewed"] or item["translation"] or item["original"]
            context.append(f"{marker} [{item['entry_index']}] falante {item['speaker_id']}: {current}")
        self.context_text.insert("1.0", "\n".join(context)); self.context_text.config(state="disabled")
        self._loading_line = False
        self._update_line_preview()

    def save_current(self, refresh=True):
        if not self.db or self.current_id is None: return
        save_text(self.db, self.current_id, self.translation_text.get("1.0", "end-1c"), self.reviewed_text.get("1.0", "end-1c"))
        if refresh:
            self.refresh()
        self.status.set("Linha salva; use 'Marcar como revisado' para aprovar o texto final")

    def copy_translation(self):
        self.reviewed_text.delete("1.0", "end")
        self.reviewed_text.insert("1.0", self.translation_text.get("1.0", "end-1c"))
        self.save_current()

    def approve_current(self):
        if not self.db or self.current_id is None:
            return
        try:
            mark_reviewed(
                self.db, self.current_id,
                self.translation_text.get("1.0", "end-1c"),
                self.reviewed_text.get("1.0", "end-1c"),
            )
        except ValueError as exc:
            messagebox.showerror("Revisão", str(exc))
            return
        self.refresh()
        self.status.set("Texto final aprovado e registrado com origem e horário")

    def clear_reviewed(self):
        if self.current_id is None:
            return
        self.reviewed_text.delete("1.0", "end")
        self.save_current()

    def close_window(self):
        if self._autosave_job is not None:
            self.after_cancel(self._autosave_job)
            self._autosave_job = None
        if self.db and self.current_id is not None:
            save_text(
                self.db, self.current_id,
                self.translation_text.get("1.0", "end-1c"),
                self.reviewed_text.get("1.0", "end-1c"),
            )
        if self.db:
            self.db.close()
        self.destroy()

    def configure_api(self):
        dialog = tk.Toplevel(self); dialog.title("Azure / DeepL"); dialog.transient(self); dialog.grab_set()
        values = {"provider":tk.StringVar(value="DeepL"), "key":tk.StringVar(), "region":tk.StringVar(value="global"),
                  "endpoint":tk.StringVar(), "cpm":tk.StringVar(value="30000"),
                  "batch_chars":tk.StringVar(value="8000"), "batch_items":tk.StringVar(value="50"),
                  "deepl_context":tk.StringVar(value="8000"),
                  "glossary":tk.StringVar(value=self.glossary_path), "category":tk.StringVar()}
        fields = (("Serviço", "provider"), ("Chave da API", "key"), ("Região Azure", "region"),
                  ("Endpoint personalizado (opcional)", "endpoint"), ("Azure caracteres/minuto", "cpm"),
                  ("Caracteres máximos por lote", "batch_chars"), ("Itens máximos por lote", "batch_items"),
                  ("DeepL: caracteres máximos de contexto", "deepl_context"),
                  ("Glossário Azure CSV", "glossary"), ("Categoria Azure personalizada", "category"))
        for i,(label,key) in enumerate(fields):
            ttk.Label(dialog,text=label).grid(row=i,column=0,sticky="w",padx=8,pady=5)
            if key=="provider": widget=ttk.Combobox(dialog,textvariable=values[key],values=("DeepL","Azure"),state="readonly")
            else: widget=ttk.Entry(dialog,textvariable=values[key],width=55,show="*" if key=="key" else "")
            widget.grid(row=i,column=1,padx=8,pady=5)
            if key == "glossary":
                ttk.Button(
                    dialog, text="Escolher...",
                    command=lambda: values["glossary"].set(
                        filedialog.askopenfilename(
                            title="Selecione o glossário",
                            filetypes=(("Glossário CSV", "*.csv"), ("Todos", "*.*")),
                        ) or values["glossary"].get()
                    ),
                ).grid(row=i, column=2, padx=(0, 8), pady=5)
        def save():
            try:
                cpm = int(values["cpm"].get())
                batch_chars = int(values["batch_chars"].get())
                batch_items = int(values["batch_items"].get())
                deepl_context = int(values["deepl_context"].get())
                if min(cpm, batch_chars, batch_items) <= 0 or deepl_context < 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror(
                    "Configuração",
                    "Lotes e velocidade devem ser inteiros positivos; o contexto pode ser zero.",
                )
                return
            self.translation_config = TranslationConfig(
                provider=values["provider"].get(), api_key=values["key"].get().strip(),
                region=values["region"].get().strip(), endpoint=values["endpoint"].get().strip(),
                azure_chars_per_minute=cpm, batch_characters=batch_chars, batch_items=batch_items,
                glossary_path=values["glossary"].get().strip(),
                azure_category=values["category"].get().strip(),
                deepl_context_characters=deepl_context,
            )
            self.glossary_path = self.translation_config.glossary_path
            dialog.destroy(); self.status.set(f"API configurada: {self.translation_config.provider}")
        ttk.Button(dialog,text="Usar nesta sessão",command=save).grid(row=len(fields),column=1,sticky="e",padx=8,pady=10)

    def start_translation(self):
        if not self.project_path or not self.translation_config:
            messagebox.showinfo("Configuração", "Abra um projeto e configure Azure ou DeepL primeiro."); return
        if not self.translation_config.api_key:
            messagebox.showerror("Chave", "Informe a chave da API."); return
        pending = self.db.execute(
            "SELECT COUNT(*),COALESCE(SUM(length(original)),0) FROM dialogues "
            "WHERE automatic='' AND translation='' AND locked=0"
        ).fetchone()
        if not pending[0]:
            messagebox.showinfo("Tradução", "Não há textos pendentes para enviar ao provedor.")
            return
        if not messagebox.askokcancel(
            "Confirmar consumo da API",
            f"Provedor: {self.translation_config.provider}\n"
            f"Textos pendentes: {pending[0]}\n"
            f"Estimativa de caracteres de origem: {pending[1]:,}\n"
            f"Limite por lote: {self.translation_config.batch_items} itens / "
            f"{self.translation_config.batch_characters:,} caracteres\n\n"
            f"Contexto DeepL por cena: até {self.translation_config.deepl_context_characters:,} caracteres\n\n"
            "A resposta original será preservada separadamente da tradução editável.",
        ):
            return
        backup = backup_project(self.db, self.project_path, "antes_traducao_automatica")
        self.stop_requested=False; self.status.set("Tradução em andamento; cada lote é salvo automaticamente...")
        def work():
            db=connect(self.project_path)
            try:
                return run_queue(db,self.translation_config,
                    lambda total,_: self.after(0, lambda: (
                        self.status.set(f"Traduzidas nesta sessão: {total}"),
                        self._refresh_progress_panel(),
                    )),
                    lambda:self.stop_requested)
            finally: db.close()
        self._background(work, lambda count:(
            self.refresh(),
            self.status.set(f"Tradução encerrada: {count} linhas salvas; backup: {backup.name}"),
        ))

    def export_reports(self):
        if not self.project_path or not self.db:
            return
        output = filedialog.askdirectory(title="Pasta para CSV e relatórios")
        if not output:
            return
        self.status.set("Exportando planilha e relatórios...")
        def work():
            db = connect(self.project_path)
            try:
                return export_project_reports(db, self.project_path, Path(output))
            finally:
                db.close()
        self._background(
            work,
            lambda result: (
                self.status.set(
                    f"Exportados {result['rows']} textos; {result['reviewed']} revisados; "
                    f"{result['review_drafts_count']} aguardando aprovação; "
                    f"{result['oversized_count']} acima dos bytes"
                ),
                messagebox.showinfo("Exportação concluída", f"Arquivos salvos em:\n{output}"),
            ),
        )

    def import_csv(self):
        if not self.project_path or not self.db:
            return
        source = filedialog.askopenfilename(
            title="Importar planilha mestre",
            filetypes=(("Planilha CSV", "*.csv"), ("Todos", "*.*")),
        )
        if not source:
            return
        if not messagebox.askokcancel(
            "Importar CSV",
            "A tradução em edição e o texto final serão importados por arquivo e ID.\n"
            "A resposta original da API não será substituída.\n"
            "Aprovações só serão preservadas quando estado e hash forem válidos.\n\n"
            "Um backup será criado antes da importação.",
        ):
            return
        backup = backup_project(self.db, self.project_path, "antes_importar_csv")
        self.status.set("Validando e importando CSV...")

        def work():
            db = connect(self.project_path)
            try:
                return import_project_csv(db, Path(source))
            finally:
                db.close()

        self._background(
            work,
            lambda result: (
                self.refresh(),
                self.status.set(
                    f"CSV importado: {result['updated']} linhas; {result['approved']} aprovadas; "
                    f"{result['drafts']} aguardando revisão; backup: {backup.name}"
                ),
            ),
        )

    def generate_iso(self):
        if not self.project_path or not self.db: return
        if self.current_id is not None:
            save_text(
                self.db,
                self.current_id,
                self.translation_text.get("1.0", "end-1c"),
                self.reviewed_text.get("1.0", "end-1c"),
            )
            self.refresh()
        counts = planned_iso_counts(self.db)
        if not counts["reviewed"] and not counts["automatic"]:
            messagebox.showinfo(
                "Nenhuma tradução aplicável",
                "Ainda não há texto final aprovado nem resposta automática válida.\n\n"
                f"Há {counts['drafts']} textos finais sem aprovação explícita.\n"
                "Traduções em edição e rascunhos não são aplicados.",
            )
            return
        if not messagebox.askokcancel(
            "Gerar com revisão e fallback automático",
            f"Textos selecionados: {counts['reviewed']} revisados aprovados, "
            f"{counts['automatic']} automáticos e {counts['original']} originais.\n"
            f"{counts['drafts']} textos finais sem aprovação não substituirão a resposta automática.\n\n"
            f"{counts['oversized']} excedem o limite conservador da linha original; "
            "a capacidade real do EVD será validada antes da gravação.\n\n"
            "Traduções em edição não são usadas até serem aprovadas como texto final.",
        ):
            return
        output=filedialog.asksaveasfilename(defaultextension=".iso",filetypes=(("Imagem ISO","*.iso"),))
        if not output:return
        backup = backup_project(self.db, self.project_path, "antes_gerar_iso")
        self.status.set("Copiando e reconstruindo a ISO...")
        relocate = messagebox.askyesno(
            "Textos maiores — realocação experimental",
            "Realocar os arquivos de diálogo para permitir textos maiores?\n\n"
            "A ISO ficará maior. Inclui o prólogo, sem limite por registro original.\n"
            "A estrutura será conferida com a regra de leitura do jogo.\n"
            "A expansão precisa ser testada no jogo e não aumenta a caixa visual.\n\n"
            "Sim: expandir diálogos. Não: manter limites originais.",
        )
        relocate_strings = messagebox.askyesno(
            "Textos do executável — teste experimental",
            "Tentar realocar textos maiores de itens, menus e falas do executável?\n\n"
            "Reutiliza somente espaço de textos menores e altera referências em tabelas. "
            "Não injeta código nem amplia a memória. Casos ambíguos continuam no original.\n\n"
            "Ainda exige teste no jogo: início, inventário, menus e batalha. "
            "Guarde a ISO anterior que funcionou.\n\nSim: gerar variante de teste. Não: manter fluxo anterior.",
        )
        expand_arena = False
        if relocate_strings:
            expand_arena = messagebox.askyesno(
                "Banco adicional — experimental, teste desde o início",
                "Criar espaço adicional para as traduções completas do executável?\n\n"
                "Reserva até 1 MiB da memória dinâmica e ajusta sua inicialização. "
                "Pode causar falta de memória em cenas ainda não testadas. "
                "Referências não reconhecidas permanecem no original.\n\n"
                "Preserve a ISO anterior. Inicie a nova ISO do zero; não restaure um savestate antigo. "
                "Teste Novo Jogo, memory card, inventário e batalhas.\n\n"
                "Sim: banco adicional. Não: somente reorganização anterior.",
                default=messagebox.NO,
            )
        self._background(lambda:build_iso(self.project_path,Path(output),"native-menu-font",relocate=relocate,relocate_strings=relocate_strings,expand_text_arena=expand_arena),
            lambda result:(
                self.status.set(
                    f"ISO criada: {result['verified_lines']} linhas verificadas; "
                    f"{result['capacity_fallback_count']} retornaram ao original por espaço"
                ),
                messagebox.showinfo(
                    "Concluído",
                    f"{result['lines']} linhas traduzidas foram aplicadas.\n"
                    f"{result['verified_lines']} foram reabertas e conferidas na ISO.\n"
                    f"Vídeos PT-BR aplicados e conferidos: {result['movies_applied']}.\n"
                    f"Fonte portuguesa: {'incluída' if result['portuguese_font'] else 'não necessária'}.\n"
                    f"Arquivos realocados: {result['relocated_files']}.\n"
                    f"Textos realocados no executável (experimental): {result['relocated_strings']}.\n"
                    f"Banco adicional: {result['text_arena'].get('capacity_bytes',0)} bytes; "
                    f"reserva de memória: {result['text_arena'].get('heap_reserved_bytes',0)} bytes.\n"
                    "Origem dos textos: "
                    f"{result['selection_counts']['reviewed']} revisados, "
                    f"{result['selection_counts']['automatic']} automáticos, "
                    f"{result['selection_counts']['original']} originais.\n"
                    f"Fallback por capacidade: {result['capacity_fallback_count']} respostas automáticas "
                    "voltaram ao original por limite ou referência não comprovada, sem cortar texto.\n"
                    f"Relatório de fallback: {result['capacity_fallback_report']}\n"
                    f"Backup do projeto: {backup.name}\n"
                    f"SHA-256: {result['output_sha256']}\n\n"
                    f"{result['output']}",
                ),
            ))


def run(initial_project: Path | None = None):
    MainWindow(initial_project).mainloop()
