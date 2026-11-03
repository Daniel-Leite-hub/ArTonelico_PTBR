"""Extract from the Japanese ISO only the video files that received subtitles in the English release.
"""
from pathlib import Path
import json
import hashlib
import sys

# Ensure artonelico_tool is accessible
root_dir = Path(__file__).resolve().parents[1]
workspace_dir = root_dir.parent
sys.path.insert(0, str(root_dir))

from artonelico_tool.iso import list_files, read_entry, find, SECTOR

JP_ISO_PATH = workspace_dir / "Ar tonelico - Sekai no Owari de Utai Tsuzukeru Shoujo (Japan) (PlayStation 2 the Best).iso"
EN_ISO_PATH = workspace_dir / "Ar tonelico - Melody of Elemia (Undub).iso"
MANIFEST_EN_PATH = root_dir / "release/videos_ptbr/manifest.json"
OUTPUT_DIR = root_dir / "Videos_originais_JP_SFD"


def main():
    if not JP_ISO_PATH.exists():
        raise FileNotFoundError(f"Japanese ISO not found: {JP_ISO_PATH}")
    if not MANIFEST_EN_PATH.exists():
        raise FileNotFoundError(f"Subtitled manifest not found: {MANIFEST_EN_PATH}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    manifest_data = json.loads(MANIFEST_EN_PATH.read_text(encoding="utf-8"))
    subtitled_movies = manifest_data.get("movies", [])
    print(f"Subtitled movies defined in manifest: {len(subtitled_movies)}")

    jp_entries = {e.path.upper(): e for e in list_files(JP_ISO_PATH) if not e.is_dir}
    en_entries = {}
    if EN_ISO_PATH.exists():
        en_entries = {e.path.upper(): e for e in list_files(EN_ISO_PATH) if not e.is_dir}

    extracted_records = []
    total_bytes = 0

    with JP_ISO_PATH.open("rb") as fp_jp:
        for m in subtitled_movies:
            rel_path = m["iso_path"]
            entry = jp_entries.get(rel_path.upper())
            if not entry:
                raise KeyError(f"Video {rel_path} not found in Japanese ISO!")

            target_file = OUTPUT_DIR / rel_path
            target_file.parent.mkdir(parents=True, exist_ok=True)

            print(f"Extracting {rel_path} ({entry.size:,} bytes)...", end="", flush=True)
            fp_jp.seek(entry.extent * SECTOR)
            data = fp_jp.read(entry.size)

            if len(data) != entry.size:
                raise IOError(f"Read mismatch for {rel_path}: expected {entry.size}, got {len(data)}")

            if not data.startswith(b"\x00\x00\x01\xba") or b"SofdecStream" not in data[:65536]:
                raise ValueError(f"Corrupt or invalid Sofdec stream in {rel_path}")

            target_file.write_bytes(data)
            sha256 = hashlib.sha256(data).hexdigest()
            total_bytes += entry.size

            en_entry = en_entries.get(rel_path.upper())
            en_info = {
                "en_bytes": en_entry.size if en_entry else m.get("original_sha256"),
                "en_sha256": m.get("original_sha256"),
                "cues_count": len(m.get("cues", [])),
            }

            extracted_records.append({
                "path": rel_path,
                "bytes": entry.size,
                "iso_lba": entry.extent,
                "sha256": sha256,
                "header_verified": True,
                "english_comparison": en_info
            })
            print(f" OK (SHA256: {sha256[:12]}...)")

    manifest_output = {
        "source_iso": JP_ISO_PATH.name,
        "source_iso_bytes": JP_ISO_PATH.stat().st_size,
        "description": "Arquivos de video (.SFD) originais limpos extraidos da ISO Japonesa (sem legendas hardsub gravadas pela versao americana).",
        "count": len(extracted_records),
        "total_bytes": total_bytes,
        "files": extracted_records,
        "excluded_staff_credits_videos": [
            {
                "path": "MOVIE/ED/ENDING20.SFD",
                "reason": "Video de creditos finais (Staff Roll), sem falas/legendas de dialogo."
            },
            {
                "path": "MOVIE/ED/ENDING31.SFD",
                "reason": "Video de creditos finais (Staff Roll), sem falas/legendas de dialogo."
            },
            {
                "path": "MOVIE/ED/ENDING34.SFD",
                "reason": "Video de creditos finais (Staff Roll), sem falas/legendas de dialogo."
            },
            {
                "path": "MOVIE/EVENT/SYU_ED.SFD",
                "reason": "Encerramento/creditos de Shurelia (Staff Roll), sem falas/legendas de dialogo."
            },
            {
                "path": "MOVIE/OP/OP_ROLL4.SFD",
                "reason": "Staff Roll de abertura (equipe de localizacao americana), sem falas/legendas de dialogo."
            }
        ]
    }

    manifest_file = OUTPUT_DIR / "manifesto.json"
    manifest_file.write_text(json.dumps(manifest_output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n[SUCESSO] {len(extracted_records)} videos extraidos com sucesso em {OUTPUT_DIR}!")
    print(f"Tamanho total: {total_bytes:,} bytes ({total_bytes / (1024*1024):.2f} MB)")
    print(f"Manifesto salvo em: {manifest_file}")


if __name__ == "__main__":
    main()
