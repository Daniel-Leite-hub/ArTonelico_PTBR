from __future__ import annotations

import sqlite3
import unittest
from pathlib import Path
from unittest.mock import patch

from artonelico_tool.evd import build, encode_game_text, parse, validate_runtime_layout
from artonelico_tool.catalog_localization import apply_catalog_localization
from artonelico_tool.reported_corrections import CORRECTIONS, apply_reported_corrections
from artonelico_tool.text_roles import translation_track
from artonelico_tool.executable_text import extract_executable_texts
from artonelico_tool.iso import find, read_entry
from artonelico_tool.lzr import compress, decompress
from artonelico_tool.patcher import (
    effective_event_capacity, encode_fixed_slot, fit_event_to_capacity,
    fit_event_to_record_layout, selected_replacements,
)
from artonelico_tool.portuguese_font import (
    ACCENT_TO_ALIAS, GLYPH_RECTS, PORTUGUESE_GLYPHS, patch_tm2,
)
from artonelico_tool.native_menu_font import (
    ResetMenuText,
    CAVE_OFFSET, HOOK_SITE_OFFSET, NativeMenuText, hook_payload,
    native_menu_text, patch_native_menu_hook,
    reset_menu_text,
)
from artonelico_tool.project import (
    clear_all_translations, connect, mark_reviewed, planned_iso_counts,
    project_stats, save_text, text_digest,
)
from artonelico_tool.quality import (
    ensure_default_glossary, normalize_translation_source, protect_azure_text,
    read_glossary, restore_azure_text,
)
from artonelico_tool.reports import export_project_reports, import_project_csv
from artonelico_tool.rpk import read_index
from artonelico_tool.translator import (
    TranslationConfig, build_deepl_context, pending_batches, run_queue, translate_batch,
)


ROOT = Path(__file__).resolve().parents[1]
TEST_OUTPUT = ROOT / "work" / "test_output"


class FormatTests(unittest.TestCase):
    def test_item_acquisition_formats_preserve_runtime_substitutions(self):
        import re
        db = connect(ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj')
        original_elf = (ROOT / 'work/SLUS_214.45').read_bytes()
        cases = {
            28463: ((123,), 'Obteve 123 Cole.'),
            28465: ((encode_game_text('2')[:-1], encode_game_text('Lenço')[:-1]), 'Obteve 2 [Lenço].'),
            28466: ((encode_game_text('Filé dragão')[:-1],), 'Obteve [Filé dragão].'),
            29637: ((encode_game_text('Lenço')[:-1],), 'Item obtido: [Lenço]'),
        }
        try:
            for entry_id, (arguments, expected) in cases.items():
                row = db.execute('SELECT * FROM dialogues WHERE id=?', (entry_id,)).fetchone()
                values, _, _ = selected_replacements(db, row['event_file'], 'native-menu-font')
                payload = encode_game_text(values[row['entry_index']])
                source = original_elf[row['entry_index']:row['entry_index'] + row['original_bytes']]
                self.assertEqual(re.findall(rb'%[sd]', source), re.findall(rb'%[sd]', payload))
                rendered = payload % arguments
                self.assertNotIn(b'%s', rendered)
                self.assertNotIn(b'%d', rendered)
                expected_bytes = encode_game_text(expected)
                if entry_id == 28463:
                    expected_bytes = expected_bytes.replace(encode_game_text('123')[:-1], b'123')
                self.assertEqual(expected_bytes, rendered)
            # Literal percentages in ordinary text must not become formats.
            self.assertNotIn(b'%s', encode_game_text('Texto %s literal'))
        finally:
            db.close()

    def test_editorial_effects_preserve_values_and_damage_types(self):
        from artonelico_tool.manual_effects import effect_translation
        self.assertEqual('[Magia vermelha]CRAdiciona 30% do dano base como dano de raio.',effect_translation('[Red Magic]CRBase damage x30% in lightning damage.'))
        self.assertEqual('[Equipamento]CRAtaque +50%, defesa -50%.',effect_translation('[Equipment]CRAttack power 50% up, defense 50% down.'))
        self.assertIsNone(effect_translation('[Equipment]CRUnknown effect.'))

    def test_editorial_snapshot_has_complete_encodable_mapping_and_controls(self):
        import json,re
        from artonelico_tool.manual_effects import effect_translation
        from artonelico_tool.project import encoded_size
        texts=json.loads((ROOT/'work/manual_pending_snapshot.json').read_text(encoding='utf-8'))
        targets={}
        for path in (ROOT/'localization_manual').glob('*.txt'):
            for line in path.read_text(encoding='utf-8').splitlines():
                if not line or line.startswith('#'): continue
                key,value=line.split('|',1)
                self.assertNotIn(int(key),targets)
                targets[int(key)]=value
        tokens=re.compile(r'IM[0-9]{2}|CR|%[a-zA-Z]|#[01][A-Za-z0-9_./-]*')
        for index,source in enumerate(texts):
            target=targets.get(index) or effect_translation(source)
            self.assertIsNotNone(target,index)
            self.assertIsNotNone(encoded_size(target),index)
            self.assertEqual(tokens.findall(source),tokens.findall(target),index)

    def test_relocation_plan_keeps_index_order_and_sector_alignment(self):
        from artonelico_tool.rpk import RpkEntry
        from artonelico_tool.relocation import plan_rpk
        entries=[RpkEntry('Event/a.evd',0,100,0),RpkEntry('Event/b.evd',1,100,12)]
        plans,size=plan_rpk(entries,4096,[(0,b'x'*3000,4096)])
        self.assertEqual([0,4096],[p[1] for p in plans])
        self.assertEqual(6144,size)
        self.assertEqual(2048,plans[1][4])

    def test_native_bitmap_patch_changes_only_declared_font_data(self):
        from artonelico_tool.native_bitmap_font import patch_native_menu_font, MAP, BANK, METRICS, SLOTS
        from artonelico_tool.native_menu_font import NATIVE_MENU_CODES
        original = (ROOT / 'work/SLUS_214.45').read_bytes()
        modified = bytearray(original)
        changes = patch_native_menu_font(modified, [])
        restored = bytearray(modified)
        for offset, value in changes:
            restored[offset:offset+len(value)] = original[offset:offset+len(value)]
        self.assertEqual(original, restored)
        self.assertEqual(len(original),len(modified))
        self.assertEqual(original[CAVE_OFFSET:CAVE_OFFSET+1024],modified[CAVE_OFFSET:CAVE_OFFSET+1024])
        for (character,code),slot in zip(NATIVE_MENU_CODES.items(),SLOTS):
            self.assertEqual(code,modified[MAP+slot*2:MAP+slot*2+2])
            self.assertTrue(any(modified[BANK+slot*288:BANK+(slot+1)*288]))
        untouched = bytearray(original)
        with self.assertRaises(ValueError):
            patch_native_menu_font(untouched,[original[MAP+SLOTS[0]*2:MAP+SLOTS[0]*2+2]])
        self.assertEqual(original,untouched)

    def test_native_bitmap_patch_preserves_editorial_curly_quote(self):
        from artonelico_tool.native_bitmap_font import patch_native_menu_font, MAP, BANK, METRICS, SLOTS
        original = (ROOT / 'work/SLUS_214.45').read_bytes()
        self.assertEqual(b'\x81\x65', original[MAP+268*2:MAP+269*2])
        self.assertNotIn(268, SLOTS)
        self.assertEqual(len(SLOTS), len(set(SLOTS)))
        catalog = [encode_game_text('A palavra ‘coluna’.'), encode_game_text('Que história de ‘Classe D’?')]
        modified = bytearray(original)
        patch_native_menu_font(modified, catalog)
        for start, size in ((MAP+268*2,2),(BANK+268*288,288),(METRICS+268*2,2)):
            self.assertEqual(original[start:start+size], modified[start:start+size])
        untouched = bytearray(original)
        with self.assertRaises(ValueError):
            patch_native_menu_font(untouched, [original[MAP+275*2:MAP+276*2]])
        self.assertEqual(original, untouched)

    def test_translation_routes_and_curated_fixed_slot(self):
        self.assertEqual("localization", translation_track("SLUS/TEXT/0001", 0x86D000))
        self.assertEqual("dialogue", translation_track("SLUS/TEXT/0001", 0x86D418))
        self.assertEqual("localization", translation_track("SLUS/TEXT/0543", 0x977548))
        self.assertEqual("dialogue", translation_track("SLUS/TEXT/0543", 0x977F48))
        self.assertEqual("dialogue", translation_track("SLUS/TEXT/0300", 0x869C28))
        self.assertEqual("localization", translation_track("SLUS/TEXT/0400", 0x930698))
        self.assertEqual("dialogue", translation_track("SLUS/TEXT/0400", 0x933288))
        self.assertEqual("dialogue", translation_track("Event/107.evd", 0))
        with sqlite3.connect(":memory:") as db:
            db.row_factory = sqlite3.Row
            db.execute("CREATE TABLE dialogues (id INTEGER PRIMARY KEY, original TEXT, original_bytes INTEGER, translation_track TEXT, locked INTEGER, automatic TEXT, translation TEXT, reviewed TEXT, translated_bytes INTEGER, size_ok INTEGER, provider TEXT, error TEXT)")
            db.executemany("INSERT INTO dialogues(id,original,original_bytes,translation_track,locked,automatic,translation,reviewed,translated_bytes,size_ok,provider,error) VALUES(?,?,?,?,0,'','','',0,1,'','')", [(1,"Weapon",len(encode_game_text("Weapon")),"localization"),(2,"Weapon",4,"localization"),(3,"Weapon",30,"dialogue")])
            db.execute("INSERT INTO dialogues(id,original,original_bytes,translation_track,locked,automatic,translation,reviewed,translated_bytes,size_ok,provider,error) VALUES(4,'K-BLADE',7,'localization',1,'','','',0,1,'','')")
            result = apply_catalog_localization(db)
            self.assertEqual(1, result["localized"])
            self.assertEqual(1, result["over_capacity_saved"])
            self.assertEqual(1, result["protected_identifier"])
            self.assertEqual("Arma", db.execute("SELECT automatic FROM dialogues WHERE id=1").fetchone()[0])
            oversized = db.execute("SELECT automatic,size_ok FROM dialogues WHERE id=2").fetchone()
            self.assertEqual(("Arma", 0), tuple(oversized))
            self.assertEqual("", db.execute("SELECT automatic FROM dialogues WHERE id=3").fetchone()[0])
            protected = db.execute("SELECT automatic,locked,provider FROM dialogues WHERE id=4").fetchone()
            self.assertEqual(("K-BLADE", 1, "identificador_tecnico"), tuple(protected))

    def test_no_pending_short_manual_catalog_terms(self):
        db = sqlite3.connect(ROOT / "release/ArTonelico_PTBR.atproj")
        pending = [
            original for (original,) in db.execute(
                "SELECT original FROM dialogues WHERE translation_track='localization' "
                "AND locked=0 AND automatic='' AND translation='' AND reviewed=''"
            ) if len(original.split()) <= 3
        ]
        db.close()
        self.assertEqual([], pending)

    def test_reported_runtime_corrections_fit_their_slots(self):
        source = connect(ROOT / "ArTonelico_PTBR.atproj")
        db = sqlite3.connect(":memory:")
        source.backup(db)
        source.close()
        db.row_factory = sqlite3.Row
        try:
            result = apply_reported_corrections(db)
            self.assertGreaterEqual(result["updated"], len(CORRECTIONS))
            for original, (target, _provider) in CORRECTIONS.items():
                row = db.execute(
                    "SELECT automatic,original_bytes,size_ok FROM dialogues WHERE original=?",
                    (original,),
                ).fetchone()
                self.assertEqual(target, row["automatic"])
                self.assertLessEqual(len(encode_game_text(target)), row["original_bytes"])
                self.assertEqual(1, row["size_ok"])
                if original == "Dragon Fillet":
                    self.assertLessEqual(
                        len(encode_game_text(target)), len(encode_game_text(original))
                    )
        finally:
            db.close()

    def test_menu_renderer_never_receives_portuguese_font_escape(self):
        db = connect(ROOT / "release/ArTonelico_PTBR.atproj")
        try:
            item, _counts, _sources = selected_replacements(
                db, "SLUS/TEXT/0160", "portuguese-font"
            )
            topic, _counts, _sources = selected_replacements(
                db, "SLUS/TEXT/0339", "portuguese-font"
            )
            dialogue, _counts, _sources = selected_replacements(
                db, "SLUS/TEXT/0262", "portuguese-font"
            )
            self.assertEqual("File dragao", item[0x8653F8])
            self.assertEqual("A relacao entre Spica e Misha", topic[0x8D7158])
            self.assertIn("à beira", dialogue[0x8A3688])
            self.assertNotIn(b"#1", encode_game_text(item[0x8653F8]))
            self.assertNotIn(b"#1", encode_game_text(topic[0x8D7158]))
            self.assertIn(b"#1", encode_game_text(dialogue[0x8A3688]))
        finally:
            db.close()

    def test_native_menu_mode_uses_reserved_two_byte_codes_without_escape(self):
        db = connect(ROOT / "release/ArTonelico_PTBR.atproj")
        try:
            item, _counts, _sources = selected_replacements(
                db, "SLUS/TEXT/0160", "native-menu-font"
            )
            value = item[0x8653F8]
            encoded = encode_game_text(value)
            self.assertIsInstance(value, NativeMenuText)
            self.assertEqual("Filé dragão", value)
            self.assertNotIn(b"#1", encoded)
            self.assertIn(b"\xe0\x44", encoded)  # é
            self.assertIn(b"\xe0\x43", encoded)  # ã
        finally:
            db.close()

    def test_unsafe_native_menu_hook_is_blocked_before_any_mutation(self):
        original = (ROOT / "work/SLUS_214.45").read_bytes()
        executable = bytearray(original)
        with self.assertRaisesRegex(ValueError, "dados ativos"):
            patch_native_menu_hook(executable)
        self.assertEqual(original, executable)

    def test_native_menu_encoder_leaves_unaccented_text_in_original_font(self):
        encoded = encode_game_text(native_menu_text("File dragao"))
        self.assertEqual(encoded, encode_game_text("File dragao"))

    def test_menu_reset_mode_restores_native_font_after_every_accent(self):
        encoded = encode_game_text(reset_menu_text("Filé dragão"))
        self.assertEqual(2, encoded.count(b"#1"))
        self.assertEqual(2, encoded.count(b"#0"))
        self.assertIn(b"#1" + ACCENT_TO_ALIAS["é"].encode("ascii") + b"#0", encoded)
        self.assertIn(b"#1" + ACCENT_TO_ALIAS["ã"].encode("ascii") + b"#0", encoded)

        db = connect(ROOT / "release/ArTonelico_PTBR.atproj")
        try:
            item, _counts, _sources = selected_replacements(
                db, "SLUS/TEXT/0160", "menu-font-reset"
            )
            self.assertIsInstance(item[0x8653F8], ResetMenuText)
        finally:
            db.close()

    def test_every_extracted_evd_round_trips_exactly(self):
        paths = list((ROOT / "work/extracted/Event").glob("*.evd"))
        self.assertEqual(976, len(paths))
        count = 0
        for path in paths:
            source = path.read_bytes()
            evd = parse(source)
            count += len(evd.dialogues)
            self.assertEqual(source, build(evd), path.name)
            self.assertEqual(len(source) - len(evd.trailer), validate_runtime_layout(source, evd))
            self.assertTrue(all(not row.extra for row in evd.dialogues), path.name)
        self.assertEqual(20_304, count)

    def test_evd_runtime_padding_all_four_residues(self):
        evd = parse((ROOT / 'work/extracted/Event/5.evd').read_bytes())
        values = ['a', 'aa', 'é', 'éa']
        self.assertEqual({0, 1, 2, 3}, {len(encode_game_text(v)) % 4 for v in values})
        for value in values:
            payload = build(evd, {0: value})
            parsed = parse(payload)
            encoded = encode_game_text(value)
            self.assertEqual(4 - len(encoded) % 4, len(parsed.dialogues[0].padding))
            self.assertEqual(encoded, parsed.dialogues[0].raw)
            self.assertEqual(evd.trailer, parsed.trailer)
            self.assertEqual(len(payload) - len(evd.trailer), validate_runtime_layout(payload, evd))
        payload = build(evd, {0: 'é'})  # encoded length 4 requires 4 more bytes
        broken = payload[:32] + payload[36:]
        with self.assertRaisesRegex(ValueError, 'runtime header'):
            validate_runtime_layout(broken, evd)

    def test_evd_full_current_translations_follow_native_loader(self):
        db = connect(ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj')
        try:
            for path in (ROOT / 'work/extracted/Event').glob('*.evd'):
                evd = parse(path.read_bytes())
                replacements, _, _ = selected_replacements(db, 'Event/' + path.name, 'native-menu-font')
                payload = build(evd, replacements)
                validate_runtime_layout(payload, evd)
                parsed = parse(payload)
                for index, text in replacements.items():
                    self.assertEqual(encode_game_text(text), parsed.dialogues[index].raw)
        finally:
            db.close()

    def test_prologue_can_expand_without_truncation(self):
        evd = parse((ROOT / 'work/extracted/Event/1.evd').read_bytes())
        text = 'Esta fala mantém todas as informações. ' * 30
        payload = build(evd, {0: text})
        self.assertGreater(len(encode_game_text(text)), evd.dialogues[0].encoded_length)
        validate_runtime_layout(payload, evd)
        self.assertEqual(encode_game_text(text), parse(payload).dialogues[0].raw)

    def test_rpk_index(self):
        entries = read_index(ROOT / "work/SLUS_214.45", (ROOT / "work/RPK.BIN").stat().st_size)
        self.assertEqual(2_703, len(entries))
        self.assertEqual(976, sum(entry.name.endswith(".evd") for entry in entries))

    def test_replacement_updates_length(self):
        path = ROOT / "work/extracted/Event/0.evd"
        evd = parse(path.read_bytes())
        output = build(evd, {0: "Teste."})
        changed = parse(output)
        self.assertEqual("Teste.", changed.dialogues[0].text)
        self.assertEqual(len(encode_game_text("Teste.")), changed.dialogues[0].encoded_length)

    def test_project_was_imported(self):
        db = sqlite3.connect(ROOT / "release/ArTonelico_PTBR.atproj")
        self.assertEqual(32_853, db.execute("SELECT COUNT(*) FROM dialogues").fetchone()[0])
        db.close()

    def test_executable_text_bank_contains_missing_dialogue(self):
        iso = ROOT / "Ar tonelico - Melody of Elemia (Undub).iso"
        if not iso.exists():
            iso = ROOT.parent / iso.name
        executable = read_entry(iso, find(iso, "SLUS_214.45"))
        texts = extract_executable_texts(executable)
        self.assertEqual(12_549, len(texts))
        target = next(
            item for item in texts if item.text.startswith("A ridiculously high place")
        )
        self.assertEqual(0x8A3688, target.offset)
        self.assertEqual(168, target.encoded_length)
        self.assertIn("Seagull Port", target.text)
        translated = "Um lugar muito alto, à beira do Porto Seagull... no que pensava!?"
        slot = encode_fixed_slot(translated, target.encoded_length)
        self.assertEqual(target.encoded_length, len(slot))
        self.assertTrue(slot.startswith(encode_game_text(translated)))
        with self.assertRaisesRegex(ValueError, "limite fixo"):
            encode_fixed_slot(translated * 10, target.encoded_length)

    def test_lzr_compressor_round_trip(self):
        source = (ROOT / "work/fonts/FO_HGGBP.tm2").read_bytes()
        packed = compress(source)
        self.assertEqual(source, decompress(packed))
        self.assertLessEqual(len(packed), 3 * 2048)

    def test_portuguese_library_encodes_every_glyph(self):
        encoded = encode_game_text(PORTUGUESE_GLYPHS)
        expected = b"".join(b"#1" + alias.encode("ascii") for alias in ACCENT_TO_ALIAS.values()) + b"\0"
        self.assertEqual(expected, encoded)

    def test_portuguese_mode_preserves_shift_jis_pair_alignment(self):
        encoded = encode_game_text("Este é o Portão.")
        self.assertFalse(encoded.startswith(b"#1"))
        self.assertIn(b"#1" + ACCENT_TO_ALIAS["é"].encode("ascii"), encoded)
        self.assertIn(b"#1" + ACCENT_TO_ALIAS["ã"].encode("ascii"), encoded)
        self.assertEqual(2, encoded.count(b"#1"))

    def test_consecutive_portuguese_glyphs_each_receive_marker(self):
        encoded = encode_game_text("ção")
        self.assertEqual(
            b"#1" + ACCENT_TO_ALIAS["ç"].encode("ascii")
            + b"#1" + ACCENT_TO_ALIAS["ã"].encode("ascii") + "ｏ".encode("cp932") + b"\0",
            encoded,
        )

    def test_portuguese_font_still_fits_its_rpk_slot(self):
        source = (ROOT / "work/fonts/FO_HGGBP.tm2").read_bytes()
        patched, preview = patch_tm2(source)
        self.assertEqual((256, 128), preview.size)
        self.assertNotEqual(source, patched)
        self.assertLessEqual(len(compress(patched)), 3 * 2048)

    def test_lowercase_accents_share_the_unaccented_baseline(self):
        source = (ROOT / "work/fonts/FO_HGGBP.tm2").read_bytes()
        _, preview = patch_tm2(source)
        alpha = preview.getchannel("A")
        # Arial 21's ordinary lowercase body ends at row 15 in a 22 px cell.
        # The old independent centering placed á/ã/é two atlas pixels lower.
        for character in "áãéêíóôõúü":
            alias = ACCENT_TO_ALIAS[character]
            x0, y0, x1, y1 = GLYPH_RECTS[alias]
            cell = alpha.crop((x0, y0, x1, y1))
            self.assertEqual(15, cell.getbbox()[3] - 1, character)

    def test_uppercase_accents_share_the_unaccented_baseline(self):
        source = (ROOT / "work/fonts/FO_HGGBP.tm2").read_bytes()
        _, preview = patch_tm2(source)
        alpha = preview.getchannel("A")
        # Uppercase and lowercase letters share the same row-15 baseline in
        # game.  The diacritic stays above while the capital body is composed
        # separately instead of being centered as one tall glyph.
        for character in "ÁÀÂÃÉÊÍÓÔÕÚÜ":
            alias = ACCENT_TO_ALIAS[character]
            x0, y0, x1, y1 = GLYPH_RECTS[alias]
            cell = alpha.crop((x0, y0, x1, y1))
            self.assertEqual(15, cell.getbbox()[3] - 1, character)
            self.assertIsNotNone(
                cell.crop((0, 0, cell.width, 2)).getbbox(), character
            )

    def test_portuguese_aliases_use_compatible_advances(self):
        advances = {
            character: GLYPH_RECTS[alias][2] - GLYPH_RECTS[alias][0]
            for character, alias in ACCENT_TO_ALIAS.items()
        }
        for family in ("áàâã", "éê", "óôõ", "úü", "ÁÀÂÃ", "ÉÊ", "ÓÔÕ", "ÚÜ"):
            widths = {advances[character] for character in family}
            self.assertLessEqual(max(widths) - min(widths), 1, family)
        self.assertEqual(6, advances["í"])
        self.assertEqual(6, advances["Í"])
        self.assertLessEqual(max(advances[c] for c in "áàâãéêóôõúüç"), 15)

    def test_iso_prefers_approved_then_valid_automatic_then_original(self):
        db = sqlite3.connect(":memory:")
        db.row_factory = sqlite3.Row
        db.execute(
            "CREATE TABLE dialogues(id INTEGER PRIMARY KEY, event_file TEXT, entry_index INTEGER, "
            "original TEXT, automatic TEXT, translation TEXT, reviewed TEXT, error TEXT, "
            "review_status TEXT, reviewed_hash TEXT, locked INTEGER, original_bytes INTEGER)"
        )
        db.executemany(
            "INSERT INTO dialogues(event_file,entry_index,original,automatic,translation,reviewed,"
            "error,review_status,reviewed_hash,locked,original_bytes) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
            (
                ("Event/1.evd", 0, "Original", "Automática", "Edição", "", "", "unreviewed", "", 0, 100),
                ("Event/1.evd", 1, "Original", "Automática", "Tradução antiga", "Texto final", "", "approved", text_digest("Texto final"), 0, 100),
                ("Event/1.evd", 2, "Original", "Automática", "Outra tradução", "Rascunho", "", "draft", "", 0, 100),
                ("Event/1.evd", 3, "Original", "", "Edição", "", "", "unreviewed", "", 0, 100),
                ("Event/1.evd", 4, "Original", "Emoji 😀", "", "", "", "unreviewed", "", 0, 100),
                ("Event/1.evd", 5, "#1MARCADOR Texto", "Marcador ausente", "", "", "", "unreviewed", "", 0, 100),
                ("Event/1.evd", 6, "Original", "Automática", "", "", "", "unreviewed", "", 1, 100),
            ),
        )
        replacements, counts, _sources = selected_replacements(db, "Event/1.evd", "block")
        self.assertEqual(
            {0: "Automática", 1: "Texto final", 2: "Automática"},
            replacements,
        )
        self.assertEqual({"reviewed": 1, "automatic": 2, "original": 4}, counts)
        self.assertEqual(1, planned_iso_counts(db)["drafts"])
        db.close()

    def test_automatic_fallback_rebuilds_an_actual_evd_entry(self):
        source = (ROOT / "work/extracted/Event/0.evd").read_bytes()
        evd = parse(source)
        db = sqlite3.connect(":memory:")
        db.row_factory = sqlite3.Row
        db.execute(
            "CREATE TABLE dialogues(entry_index INTEGER, event_file TEXT, original TEXT, "
            "automatic TEXT, reviewed TEXT, review_status TEXT, reviewed_hash TEXT, locked INTEGER)"
        )
        db.execute(
            "INSERT INTO dialogues VALUES(?,?,?,?,?,?,?,?)",
            (2, "Event/0.evd", evd.dialogues[2].text, "Senhora Shurelia, o que devemos fazer?",
             "", "unreviewed", "", 0),
        )
        replacements, counts, _sources = selected_replacements(db, "Event/0.evd", "block")
        rebuilt = parse(build(evd, replacements))
        self.assertEqual({"reviewed": 0, "automatic": 1, "original": 0}, counts)
        self.assertEqual(
            encode_game_text("Senhora Shurelia, o que devemos fazer?"),
            rebuilt.dialogues[2].raw,
        )
        self.assertEqual(evd.dialogues[1].raw, rebuilt.dialogues[1].raw)
        db.close()

    def test_oversized_event_falls_back_only_automatic_text(self):
        source = (ROOT / "work/extracted/Event/0.evd").read_bytes()
        evd = parse(source)
        capacity = ((len(source) + 2047) // 2048) * 2048
        oversized = {2: "Tradução automática muito longa. " * 300}
        rebuilt, replacements, fallbacks = fit_event_to_capacity(
            evd, oversized, {2: "automatic"}, capacity
        )
        self.assertLessEqual(len(rebuilt), capacity)
        self.assertEqual({}, replacements)
        self.assertEqual([2], fallbacks)
        with self.assertRaisesRegex(ValueError, "Reduza uma revisão aprovada"):
            fit_event_to_capacity(evd, oversized, {2: "reviewed"}, capacity)

    def test_event_capacity_uses_the_available_rpk_slot(self):
        self.assertEqual(36_864, effective_event_capacity("Event/1.evd", 36_168, 36_864))
        self.assertEqual(36_864, effective_event_capacity("Event/8.evd", 12_152, 36_864))

    def test_prologue_rebuild_preserves_every_record_slot(self):
        source = (ROOT / "work/extracted/Event/1.evd").read_bytes()
        evd = parse(source)
        db = connect(ROOT / "release/ArTonelico_PTBR.atproj")
        replacements, _counts, sources = selected_replacements(
            db, "Event/1.evd", "portuguese-font"
        )
        rebuilt, fitted, fallbacks = fit_event_to_record_layout(
            evd, replacements, sources, len(source)
        )
        db.close()
        reparsed = parse(rebuilt)
        self.assertEqual(len(source), len(rebuilt))
        self.assertEqual(evd.trailer, reparsed.trailer)
        self.assertEqual(
            [row.encoded_length for row in evd.dialogues],
            [row.encoded_length for row in reparsed.dialogues],
        )
        self.assertEqual(
            [len(row.padding) for row in evd.dialogues],
            [len(row.padding) for row in reparsed.dialogues],
        )
        self.assertGreater(len(fitted), 0)
        self.assertEqual([], fallbacks)

    def test_project_progress_categories_cover_every_eligible_line(self):
        db = sqlite3.connect(":memory:")
        db.row_factory = sqlite3.Row
        db.execute(
            "CREATE TABLE dialogues(automatic TEXT, translation TEXT, reviewed TEXT, "
            "review_status TEXT, size_ok INTEGER, locked INTEGER, error TEXT)"
        )
        db.executemany(
            "INSERT INTO dialogues VALUES(?,?,?,?,?,?,?)",
            (
                ("Tradução válida", "Tradução válida", "", "unreviewed", 1, 0, ""),
                ("Muito longa", "Muito longa", "", "unreviewed", 0, 0, ""),
                ("", "", "Texto final", "approved", 1, 0, ""),
                ("", "", "", "unreviewed", 1, 0, ""),
                ("Inválida", "Inválida", "", "unreviewed", 0, 0, "Caractere não suportado"),
                ("", "", "", "unreviewed", 1, 1, ""),
            ),
        )
        stats = project_stats(db)
        self.assertEqual(6, stats["total"])
        self.assertEqual(5, stats["eligible"])
        self.assertEqual(2, stats["correct"])
        self.assertEqual(1, stats["errors"])
        self.assertEqual(1, stats["oversized"])
        self.assertEqual(1, stats["pending"])
        self.assertEqual(1, stats["reviewed"])
        self.assertEqual(0, stats["review_drafts"])
        self.assertEqual(
            stats["eligible"],
            stats["correct"] + stats["errors"] + stats["oversized"] + stats["pending"],
        )
        db.close()

    def test_glossary_and_azure_commands_are_preserved(self):
        TEST_OUTPUT.mkdir(parents=True, exist_ok=True)
        project = TEST_OUTPUT / "quality.atproj"
        glossary_path = project.with_suffix(".glossario.csv")
        glossary_path.unlink(missing_ok=True)
        glossary_path = ensure_default_glossary(project)
        glossary = read_glossary(glossary_path)
        self.assertIn(("Lyner", "Lyner"), glossary)
        protected, commands = protect_azure_text("Lyner usa #1MISYA_FEHU.", glossary)
        self.assertIn("mstrans:dictionary", protected)
        self.assertIn("notranslate", protected)
        self.assertEqual("Lyner usa #1MISYA_FEHU.", restore_azure_text(protected, commands))
        glossary_path.unlink(missing_ok=True)

    def test_visual_line_breaks_are_joined_before_translation(self):
        source = (
            "Find Black Metal in the depths of the " + "\\" + "\n"
            "forest west of the Yi'el Village ruins" + "\\" + "\r\n"
            "in order to activate the cannon."
        )
        self.assertEqual(
            "Find Black Metal in the depths of the forest west of the Yi'el "
            "Village ruins in order to activate the cannon.",
            normalize_translation_source(source),
        )

    def test_literal_newline_command_is_not_removed(self):
        self.assertEqual(
            r"First line\nSecond line",
            normalize_translation_source(r"First line\nSecond line"),
        )

    def test_queue_sends_joined_text_without_changing_saved_original(self):
        db = sqlite3.connect(":memory:")
        db.row_factory = sqlite3.Row
        db.execute(
            "CREATE TABLE dialogues(id INTEGER PRIMARY KEY, event_file TEXT, entry_index INTEGER, "
            "speaker_id INTEGER, original TEXT, automatic TEXT, translation TEXT, "
            "locked INTEGER, original_bytes INTEGER, "
            "translated_bytes INTEGER, size_ok INTEGER, provider TEXT, error TEXT)"
        )
        source = "The first half " + "\\" + "\n" + "continues on the next line."
        db.execute(
            "INSERT INTO dialogues VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (1, "Event/test.evd", 4, 7, source, "", "", 0, 200, 0, 0, "", ""),
        )
        db.execute("ALTER TABLE dialogues ADD COLUMN translation_track TEXT DEFAULT 'dialogue'")
        sent: list[str] = []

        received_context = []

        def fake_translate(_config, texts, azure_html=False, context=""):
            self.assertFalse(azure_html)
            sent.extend(texts)
            received_context.append(context)
            return ["A frase completa."]

        config = TranslationConfig(provider="DeepL", api_key="test")
        with patch("artonelico_tool.translator.translate_batch", side_effect=fake_translate), \
                patch("artonelico_tool.translator.time.sleep"):
            self.assertEqual(1, run_queue(db, config))

        self.assertEqual(["The first half continues on the next line."], sent)
        self.assertIn("Ar tonelico: Melody of Elemia", received_context[0])
        self.assertIn("Event/test.evd", received_context[0])
        self.assertIn("Speaker 7", received_context[0])
        self.assertEqual(source, db.execute("SELECT original FROM dialogues").fetchone()[0])
        saved = db.execute("SELECT automatic,translation FROM dialogues").fetchone()
        self.assertEqual(("A frase completa.", "A frase completa."), tuple(saved))
        db.close()

    def test_deepl_payload_receives_context_and_scene_batches_do_not_mix(self):
        db = sqlite3.connect(":memory:")
        db.row_factory = sqlite3.Row
        db.execute(
            "CREATE TABLE dialogues(id INTEGER PRIMARY KEY, event_file TEXT, entry_index INTEGER, "
            "speaker_id INTEGER, original TEXT, automatic TEXT, translation TEXT, locked INTEGER)"
        )
        db.executemany(
            "INSERT INTO dialogues VALUES(?,?,?,?,?,?,?,?)",
            (
                (1, "Event/a.evd", 0, 10, "Where is Aurica?", "", "", 0),
                (2, "Event/a.evd", 1, 11, "She went to the tower.", "", "", 0),
                (3, "Event/b.evd", 0, 12, "Open the gate.", "", "", 0),
            ),
        )
        db.execute("ALTER TABLE dialogues ADD COLUMN translation_track TEXT DEFAULT 'dialogue'")
        config = TranslationConfig(provider="DeepL", api_key="test:fx")
        db.execute(
            "INSERT INTO dialogues VALUES(?,?,?,?,?,?,?,?,?)",
            (4, "SLUS/TEXT/0001", 0x7CABC8, 0, "Item", "", "", 0, "localization"),
        )
        batches = list(pending_batches(db, config))
        self.assertEqual(2, len(batches))
        self.assertEqual({"Event/a.evd"}, {row["event_file"] for row in batches[0]})
        self.assertEqual({"Event/b.evd"}, {row["event_file"] for row in batches[1]})
        context = build_deepl_context(db, batches[0])
        self.assertIn("Where is Aurica?", context)
        self.assertIn("She went to the tower.", context)
        with patch(
            "artonelico_tool.translator._request",
            return_value={"translations": [{"text": "Onde está Aurica?"}]},
        ) as request:
            self.assertEqual(
                ["Onde está Aurica?"], translate_batch(config, ["Where is Aurica?"], context=context)
            )
        payload = request.call_args.args[1]
        self.assertEqual(context, payload["context"])
        self.assertTrue(payload["show_billed_characters"])
        db.close()

    def test_final_text_requires_explicit_approval_and_edit_invalidates_it(self):
        TEST_OUTPUT.mkdir(parents=True, exist_ok=True)
        project = TEST_OUTPUT / "review_state.atproj"
        project.unlink(missing_ok=True)
        db = connect(project)
        db.execute(
            """INSERT INTO dialogues(event_file,entry_index,text_id,speaker_id,original,
            automatic,translation,original_bytes,locked,provider)
            VALUES(?,?,?,?,?,?,?,?,?,?)""",
            ("Event/test.evd", 0, 1, 2, "Hello", "Olá", "Olá", 100, 0, "DeepL"),
        )
        row_id = db.execute("SELECT id FROM dialogues").fetchone()[0]
        mark_reviewed(db, row_id, "Olá", "Olá.")
        approved = db.execute(
            "SELECT review_status,review_origin,reviewed_hash FROM dialogues WHERE id=?", (row_id,)
        ).fetchone()
        self.assertEqual("approved", approved["review_status"])
        self.assertEqual("usuario", approved["review_origin"])
        self.assertEqual(text_digest("Olá."), approved["reviewed_hash"])
        save_text(db, row_id, "Olá", "Olá!")
        invalidated = db.execute(
            "SELECT review_status,review_origin,reviewed_hash,automatic FROM dialogues WHERE id=?",
            (row_id,),
        ).fetchone()
        self.assertEqual("draft", invalidated["review_status"])
        self.assertEqual("", invalidated["review_origin"])
        self.assertEqual("", invalidated["reviewed_hash"])
        self.assertEqual("Olá", invalidated["automatic"])
        cleared = clear_all_translations(db)
        self.assertEqual({"automatic": 1, "translation": 1, "reviewed": 1}, cleared)
        empty = db.execute(
            "SELECT automatic,translation,reviewed,review_status,provider FROM dialogues WHERE id=?",
            (row_id,),
        ).fetchone()
        self.assertEqual(("", "", "", "unreviewed", ""), tuple(empty))
        db.close()
        project.unlink(missing_ok=True)

    def test_legacy_project_is_backed_up_and_preserves_reviews(self):
        TEST_OUTPUT.mkdir(parents=True, exist_ok=True)
        project = TEST_OUTPUT / "legacy.atproj"
        project.unlink(missing_ok=True)
        backup_dir = TEST_OUTPUT / "backups" / "legacy"
        if backup_dir.exists():
            for old_backup in backup_dir.glob("*.atproj"):
                old_backup.unlink()
            backup_dir.rmdir()
        old = sqlite3.connect(project)
        old.execute(
            """CREATE TABLE dialogues(
            id INTEGER PRIMARY KEY, event_file TEXT NOT NULL, entry_index INTEGER NOT NULL,
            text_id INTEGER NOT NULL, speaker_id INTEGER NOT NULL, original TEXT NOT NULL,
            translation TEXT NOT NULL DEFAULT '', reviewed TEXT NOT NULL DEFAULT '',
            original_bytes INTEGER NOT NULL, translated_bytes INTEGER NOT NULL DEFAULT 0,
            size_ok INTEGER NOT NULL DEFAULT 1, locked INTEGER NOT NULL DEFAULT 0,
            provider TEXT NOT NULL DEFAULT '', error TEXT NOT NULL DEFAULT '')"""
        )
        old.execute(
            "INSERT INTO dialogues VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (1, "Event/legacy.evd", 0, 1, 2, "Hello", "Olá", "Olá!", 20, 10, 1, 0, "DeepL", ""),
        )
        old.commit()
        old.close()
        db = connect(project)
        row = db.execute("SELECT * FROM dialogues").fetchone()
        self.assertEqual("Olá", row["automatic"])
        self.assertEqual("approved", row["review_status"])
        self.assertEqual("legado", row["review_origin"])
        self.assertEqual(text_digest("Olá!"), row["reviewed_hash"])
        db.close()
        backups = list(backup_dir.glob("*.atproj"))
        self.assertEqual(1, len(backups))
        backups[0].unlink()
        backups[0].parent.rmdir()
        project.unlink()

    def test_exports_master_csv_and_quality_reports(self):
        TEST_OUTPUT.mkdir(parents=True, exist_ok=True)
        project = TEST_OUTPUT / "reports.atproj"
        project.unlink(missing_ok=True)
        db = connect(project)
        db.execute(
            """INSERT INTO dialogues(event_file,entry_index,text_id,speaker_id,original,
            automatic,translation,reviewed,original_bytes,translated_bytes,size_ok,provider)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",
            ("Event/1.evd", 0, 1, 0, "Hello", "Resposta Azure", "Olá, mundo", "Olá", 1, 15, 0, "Azure"),
        )
        mark_reviewed(
            db, db.execute("SELECT id FROM dialogues").fetchone()[0], "Olá, mundo", "Olá"
        )
        db.commit()
        report_dir = TEST_OUTPUT / "reports"
        result = export_project_reports(db, project, report_dir)
        self.assertEqual(1, result["rows"])
        self.assertEqual(1, result["reviewed"])
        self.assertEqual(1, result["oversized_count"])
        self.assertIn("Olá", result["csv"].read_text(encoding="utf-8-sig"))
        self.assertTrue(result["font"].is_file())
        db.execute(
            "UPDATE dialogues SET automatic='Resposta nova',translation='',reviewed='',"
            "review_status='unreviewed',review_origin='',reviewed_at='',reviewed_hash=''"
        )
        db.commit()
        imported = import_project_csv(db, result["csv"])
        self.assertEqual({"updated": 1, "approved": 1, "drafts": 0}, imported)
        restored = db.execute(
            "SELECT automatic,translation,reviewed,review_status,review_origin FROM dialogues"
        ).fetchone()
        self.assertEqual("Resposta nova", restored["automatic"])
        self.assertEqual("Olá, mundo", restored["translation"])
        self.assertEqual("Olá", restored["reviewed"])
        self.assertEqual("approved", restored["review_status"])
        self.assertEqual("importado", restored["review_origin"])
        db.close()
        project.unlink(missing_ok=True)
        for path in report_dir.iterdir():
            path.unlink()
        report_dir.rmdir()

    def test_inline_ascii_controls_and_newline_prevention(self):
        # Native inline commands must be emitted in half-width ASCII so the PS2
        # renderer executes them instead of drawing full-width letters.
        encoded_cr = encode_game_text("[Magia Vermelha]CRAumenta o dano.")
        self.assertIn(b"CR", encoded_cr)
        self.assertNotIn("ＣＲ".encode("cp932"), encoded_cr)

        # Ordinary uppercase words starting with CR must remain full-width.
        encoded_word = encode_game_text("CRIATURAS TOLAS...")
        self.assertNotIn(b"CR", encoded_word)
        self.assertIn("ＣＲ".encode("cp932"), encoded_word)

        # Button icons, font-scale/shake commands, and Hymmnos escapes must be ASCII.
        self.assertIn(b"IM04", encode_game_text("Cristal GrathnodeIM04 OKIM00"))
        self.assertIn(b"IM00", encode_game_text("Cristal GrathnodeIM04 OKIM00"))
        encoded_sc = encode_game_text("SC30Pare com isso!!1X")
        self.assertTrue(encoded_sc.startswith(b"SC30"))
        self.assertTrue(encoded_sc.endswith(b"1X\0"))
        encoded_vb = encode_game_text("VB15Aaaah!CLRE")
        self.assertTrue(encoded_vb.startswith(b"VB15"))
        self.assertTrue(encoded_vb.endswith(b"CLRE\0"))
        encoded_hym = encode_game_text("...#0Vasiyat gegis exeks suant, Lyner##...")
        self.assertIn(b"#0Vasiyat gegis exeks suant, Lyner##", encoded_hym)
        encoded_code = encode_game_text("O Código é [#1MULE_TEIWAZ_ARTONELICO].")
        self.assertIn(b"\x81m#1\x82l\x82t", encoded_code)

        # Raw \n (0x0A) desynchronizes Shift-JIS 2-byte pair alignment in the PS2
        # dialogue renderer and must always be normalized to a full-width space.
        encoded_nl = encode_game_text("Trago o relatório, senhor!\nVírus estão se proliferando!")
        self.assertNotIn(b"\n", encoded_nl)
        self.assertNotIn(b"\r", encoded_nl)
        self.assertEqual(
            encode_game_text("Trago o relatório, senhor! Vírus estão se proliferando!"),
            encoded_nl,
        )

    def test_straight_quote_and_apostrophe_conversion(self):
        # Straight quotes (0x22 and 0x27) must map to Shift-JIS curly quotes:
        # “ (8167), ” (8168), ‘ (8165), ’ (8166).
        # CP932 \uff02 (\xee\xfc) and \uff07 (\xee\xfb) do not exist in the PS2
        # font ROM/textures and render as corrupted barcode glyphs.
        encoded_double = encode_game_text('Nele estão os diagramas do "Purger".')
        self.assertNotIn(b"\xee\xfc", encoded_double)
        self.assertIn(b"\x81\x67", encoded_double)  # “
        self.assertIn(b"\x81\x68", encoded_double)  # ”
        self.assertEqual(
            encoded_double,
            encode_game_text('Nele estão os diagramas do “Purger”.'),
        )

        encoded_single = encode_game_text("Dizem que vão 'reconquistar'.")
        self.assertNotIn(b"\xee\xfb", encoded_single)
        self.assertIn(b"\x81\x65", encoded_single)  # ‘
        self.assertIn(b"\x81\x66", encoded_single)  # ’
        self.assertEqual(
            encoded_single,
            encode_game_text("Dizem que vão ‘reconquistar’."),
        )

        encoded_apostrophe = encode_game_text("Uma gota d'água.")
        self.assertNotIn(b"\xee\xfb", encoded_apostrophe)
        self.assertIn(b"\x81\x66", encoded_apostrophe)  # ’
        self.assertEqual(
            encoded_apostrophe,
            encode_game_text("Uma gota d’água."),
        )


if __name__ == "__main__":
    unittest.main()
