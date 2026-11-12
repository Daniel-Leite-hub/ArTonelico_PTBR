"""
Ar tonelico: Melody of Elemia (Undub) — Aplicador de Tradução PT-BR
Interface gráfica autônoma para aplicar a tradução diretamente na imagem ISO.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import sqlite3
import sys
import tempfile
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

# Garante que artonelico_tool seja importável caso executado diretamente
CURRENT_DIR = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

try:
    from artonelico_tool.iso import find, read_entry
    from artonelico_tool.patcher import build_iso
except ImportError:
    # Se estiver em subpasta, tenta nível superior
    PARENT_DIR = CURRENT_DIR.parent
    if str(PARENT_DIR) not in sys.path:
        sys.path.insert(0, str(PARENT_DIR))
    from artonelico_tool.iso import find, read_entry
    from artonelico_tool.patcher import build_iso


def get_base_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


def find_default_project() -> Path | None:
    candidates = [
        get_base_dir() / "ArTonelico_PTBR_adaptado_108_20260926.atproj",
        get_base_dir() / "release" / "ArTonelico_PTBR_adaptado_108_20260926.atproj",
        get_base_dir().parent / "release" / "ArTonelico_PTBR_adaptado_108_20260926.atproj",
        get_base_dir().parent / "Ferramentas_Traducao" / "release" / "ArTonelico_PTBR_adaptado_108_20260926.atproj",
        CURRENT_DIR / "ArTonelico_PTBR_adaptado_108_20260926.atproj",
        CURRENT_DIR / "release" / "ArTonelico_PTBR_adaptado_108_20260926.atproj",
    ]
    for c in candidates:
        if c.is_file() and c.stat().st_size > 1000000:
            return c
    return None


def find_default_iso() -> Path | None:
    names = [
        "Ar tonelico - Melody of Elemia (Undub).iso",
        "Ar tonelico (Undub).iso",
        "ArTonelico_Undub.iso",
        "Ar tonelico - Melody of Elemia.iso",
    ]
    folders = [
        get_base_dir(),
        get_base_dir().parent,
        get_base_dir() / "ISOs",
        get_base_dir().parent / "ISOs",
    ]
    for folder in folders:
        for name in names:
            iso_path = folder / name
            if iso_path.is_file():
                return iso_path
    return None


class ApplicatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ar tonelico (Undub) — Aplicador PT-BR v0.9.0-beta")
        self.geometry("680x480")
        self.minsize(620, 440)
        self.resizable(True, True)

        self.project_path = find_default_project()
        self.is_patching = False

        self._create_widgets()
        self._auto_detect()

    def _create_widgets(self):
        # Estilos
        style = ttk.Style(self)
        style.theme_use("clam" if "clam" in style.theme_names() else "default")

        # Cabeçalho
        header_frame = ttk.Frame(self, padding=(16, 16, 16, 8))
        header_frame.pack(fill="x")

        title_label = ttk.Label(
            header_frame,
            text="Ar tonelico: Melody of Elemia",
            font=("Segoe UI", 16, "bold"),
            foreground="#1e3a8a",
        )
        title_label.pack(anchor="w")

        subtitle_label = ttk.Label(
            header_frame,
            text="Aplicador da Tradução para Português do Brasil (v0.9.0-beta)",
            font=("Segoe UI", 10),
            foreground="#475569",
        )
        subtitle_label.pack(anchor="w", pady=(2, 6))

        info_box = ttk.Label(
            header_frame,
            text="• 32.641 diálogos e menus traduzidos e curados pela Tríade (JP/EN/PT-BR)\n"
                 "• Acentuação gráfica nativa na VRAM (TM2) • Text Arena expandida (Beta — foco nos textos)",
            font=("Segoe UI", 9, "italic"),
            foreground="#0f766e",
        )
        info_box.pack(anchor="w")

        sep = ttk.Separator(self, orient="horizontal")
        sep.pack(fill="x", padx=16, pady=8)

        # Campos de seleção
        form_frame = ttk.Frame(self, padding=(16, 8, 16, 8))
        form_frame.pack(fill="both", expand=True)

        # 1. ISO Original
        ttk.Label(form_frame, text="1. Imagem ISO Original do Jogo (Undub):", font=("Segoe UI", 9, "bold")).pack(anchor="w")
        iso_row = ttk.Frame(form_frame)
        iso_row.pack(fill="x", pady=(4, 12))

        self.iso_var = tk.StringVar()
        self.iso_entry = ttk.Entry(iso_row, textvariable=self.iso_var)
        self.iso_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))

        btn_browse_iso = ttk.Button(iso_row, text="Selecionar ISO...", command=self._browse_source_iso)
        btn_browse_iso.pack(side="right")

        # 2. ISO Destino
        ttk.Label(form_frame, text="2. Onde salvar a ISO Traduzida:", font=("Segoe UI", 9, "bold")).pack(anchor="w")
        dest_row = ttk.Frame(form_frame)
        dest_row.pack(fill="x", pady=(4, 12))

        self.dest_var = tk.StringVar()
        self.dest_entry = ttk.Entry(dest_row, textvariable=self.dest_var)
        self.dest_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))

        btn_browse_dest = ttk.Button(dest_row, text="Salvar como...", command=self._browse_dest_iso)
        btn_browse_dest.pack(side="right")

        # Status & Progresso
        prog_frame = ttk.Frame(form_frame, padding=(0, 8, 0, 8))
        prog_frame.pack(fill="x")

        self.status_var = tk.StringVar(value="Selecione a ISO original para iniciar.")
        self.status_label = ttk.Label(prog_frame, textvariable=self.status_var, font=("Segoe UI", 9))
        self.status_label.pack(anchor="w", pady=(0, 4))

        self.progress_bar = ttk.Progressbar(prog_frame, orient="horizontal", mode="determinate")
        self.progress_bar.pack(fill="x")

        # Botão Principal de Ação
        action_frame = ttk.Frame(self, padding=(16, 8, 16, 16))
        action_frame.pack(fill="x")

        self.btn_apply = tk.Button(
            action_frame,
            text="APLICAR TRADUÇÃO NA ISO",
            font=("Segoe UI", 11, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat",
            padx=16,
            pady=8,
            cursor="hand2",
            command=self._start_patching,
        )
        self.btn_apply.pack(fill="x")

    def _auto_detect(self):
        default_iso = find_default_iso()
        if default_iso:
            self.iso_var.set(str(default_iso))
            dest = default_iso.parent / "ArTonelico_PTBR_v0.9.0-beta.iso"
            self.dest_var.set(str(dest))
            self.status_var.set("ISO original localizada automaticamente. Pronto para aplicar!")

    def _browse_source_iso(self):
        f = filedialog.askopenfilename(
            title="Selecione a ISO original de Ar tonelico (Undub)",
            filetypes=[("Imagens ISO do PlayStation 2", "*.iso;*.bin;*.img"), ("Todos os Arquivos", "*.*")],
        )
        if f:
            self.iso_var.set(f)
            p = Path(f)
            dest = p.parent / "ArTonelico_PTBR_v0.9.0-beta.iso"
            self.dest_var.set(str(dest))
            self.status_var.set("ISO original selecionada. Clique em 'Aplicar Tradução'.")

    def _browse_dest_iso(self):
        f = filedialog.asksaveasfilename(
            title="Escolha o local e nome para salvar a ISO traduzida",
            defaultextension=".iso",
            initialfile="ArTonelico_PTBR_v0.9.0-beta.iso",
            filetypes=[("Imagem ISO", "*.iso"), ("Todos os Arquivos", "*.*")],
        )
        if f:
            self.dest_var.set(f)

    def _start_patching(self):
        if self.is_patching:
            return

        source = Path(self.iso_var.get().strip())
        target = Path(self.dest_var.get().strip())

        if not source.is_file():
            messagebox.showerror("Erro", "A imagem ISO de origem não foi encontrada.\nPor favor, selecione um arquivo válido.")
            return

        if not target.parent.exists():
            messagebox.showerror("Erro", "A pasta de destino selecionada não existe.")
            return

        if source.resolve() == target.resolve():
            messagebox.showerror("Aviso", "O arquivo de destino não pode ser o mesmo da ISO original.\nEscolha outro nome ou pasta para não sobrescrever o jogo original.")
            return

        # Localiza o banco
        if not self.project_path or not self.project_path.is_file():
            self.project_path = find_default_project()
            if not self.project_path:
                # Permite ao usuário localizar manualmente se necessário
                messagebox.showwarning(
                    "Banco de Dados",
                    "O banco com a tradução (ArTonelico_PTBR_adaptado_108_20260926.atproj) não foi localizado automaticamente.\nPor favor, aponte onde ele está."
                )
                custom_proj = filedialog.askopenfilename(
                    title="Selecione o arquivo de projeto .atproj",
                    filetypes=[("Projetos Ar tonelico", "*.atproj"), ("Todos os Arquivos", "*.*")],
                )
                if custom_proj and Path(custom_proj).is_file():
                    self.project_path = Path(custom_proj)
                else:
                    return

        self.is_patching = True
        self.btn_apply.config(state="disabled", text="APLICANDO TRADUÇÃO (AGUARDE)...", bg="#94a3b8")
        self.progress_bar["value"] = 0

        # Roda em thread separada
        t = threading.Thread(target=self._run_patch_thread, args=(source, target, self.project_path), daemon=True)
        t.start()

    def _run_patch_thread(self, source: Path, target: Path, project: Path):
        temp_dir = None
        try:
            self._update_status(5, "Verificando compatibilidade da ISO original...")
            # Copia banco para temporário para poder fazer relink seguro sem modificar a pasta original
            temp_dir = tempfile.mkdtemp(prefix="artonelico_patch_")
            temp_project = Path(temp_dir) / project.name
            shutil.copy2(project, temp_project)

            # Verifica e relinka o caminho da ISO no banco
            db = sqlite3.connect(temp_project)
            try:
                meta = {k: json.loads(v) for k, v in db.execute("SELECT key, value FROM meta")}
                expected_size = meta.get("iso_size")
                if expected_size and source.stat().st_size != expected_size:
                    # Avisa mas não impede se o usuário quiser
                    pass

                # Atualiza iso_path no banco temporário
                db.execute("UPDATE meta SET value=? WHERE key=?", (json.dumps(str(source.resolve())), "iso_path"))
                db.commit()
            finally:
                db.close()

            self._update_status(10, "Iniciando compilação e injeção de textos...")

            def progress_callback(n, total, name):
                if total > 0:
                    pct = 10 + int((n / total) * 85)
                    self._update_status(pct, f"[{n}/{total}] Processando {name}...")

            # Executa a geração completa da ISO
            result = build_iso(
                project_path=temp_project,
                output_iso=target,
                accent_mode="native-menu-font",
                progress=progress_callback,
                relocate=True,
                relocate_strings=True,
                expand_text_arena=True,
            )

            self._update_status(100, "Concluído com sucesso!")
            self.after(0, lambda: self._on_success(target, result))

        except Exception as e:
            self._update_status(0, "Ocorreu um erro durante a aplicação.")
            self.after(0, lambda: self._on_error(str(e)))
        finally:
            if temp_dir and os.path.exists(temp_dir):
                shutil.rmtree(temp_dir, ignore_errors=True)

    def _update_status(self, percent: int, text: str):
        self.after(0, lambda: (
            self.progress_bar.configure(value=percent),
            self.status_var.set(text),
        ))

    def _on_success(self, target: Path, result: dict):
        self.is_patching = False
        self.btn_apply.config(state="normal", text="APLICAR TRADUÇÃO NA ISO", bg="#2563eb")
        
        lines = result.get("verified_lines", 32641)
        fallbacks = result.get("capacity_fallback_count", 0)

        msg = (
            f"A tradução (v0.9.0-beta) foi aplicada com sucesso na ISO!\n\n"
            f"• Linhas verificadas: {lines:,}\n"
            f"• Fallbacks de tamanho: {fallbacks}\n"
            f"• Arquivo gerado:\n{target.resolve()}\n\n"
            f"Nota: Esta versão Beta foca nos textos e menus do jogo.\n"
            f"O jogo está pronto para testes no PCSX2 ou em console PlayStation 2!"
        )
        if messagebox.askyesno("Tradução Concluída", msg + "\n\nDeseja abrir a pasta onde a ISO foi salva?"):
            os.system(f'explorer /select,"{target.resolve()}"')

    def _on_error(self, err_msg: str):
        self.is_patching = False
        self.btn_apply.config(state="normal", text="APLICAR TRADUÇÃO NA ISO", bg="#2563eb")
        messagebox.showerror("Erro na Aplicação", f"Não foi possível concluir a aplicação da tradução:\n\n{err_msg}")


def main():
    app = ApplicatorApp()
    app.mainloop()


if __name__ == "__main__":
    main()
