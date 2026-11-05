"""Checked, same-extent SFD replacements. Originals are never modified."""
from pathlib import Path, PurePosixPath
import hashlib
import json
from .iso import find, read_entry, SECTOR
from .relocation import move_iso_file_record


def load_movie_pack(source_iso: Path, directory: Path) -> list[dict]:
    manifest = directory / 'manifest.json'
    if not manifest.exists():
        if directory.exists():
            raise ValueError('Pacote de vídeos incompleto: manifesto não encontrado')
        return []
    data = json.loads(manifest.read_text(encoding='utf-8'))
    if data.get('schema') != 1 or not isinstance(data.get('movies'), list):
        raise ValueError('Manifesto de vídeos incompatível')
    result, seen = [], set()
    for item in data['movies']:
        path = PurePosixPath(item['iso_path'])
        filename = PurePosixPath(item['file'])
        if (path.is_absolute() or '..' in path.parts or not path.parts
                or path.parts[0] != 'MOVIE' or path.suffix.upper() != '.SFD'
                or filename.is_absolute() or '..' in filename.parts
                or ':' in str(filename) or '\\' in str(filename)):
            raise ValueError('Caminho inválido no pacote de vídeos')
        if str(path).casefold() in seen:
            raise ValueError('Vídeo duplicado no manifesto')
        seen.add(str(path).casefold())
        replacement = directory.joinpath(*filename.parts)
        if not replacement.resolve().is_relative_to(directory.resolve()):
            raise ValueError('Vídeo fora da pasta do pacote')
        payload = replacement.read_bytes()
        if hashlib.sha256(payload).hexdigest() != item['sha256']:
            raise ValueError(f'Vídeo alterado ou incompleto: {replacement.name}')
        if not payload.startswith(b'\x00\x00\x01\xba') or b'SofdecStream' not in payload[:65536]:
            raise ValueError(f'Vídeo não é um SFD reconhecido: {replacement.name}')
        entry = find(source_iso, str(path))
        if len(payload) > entry.size or not payload:
            raise ValueError(f'Vídeo não cabe no espaço original: {path}')
        orig_digest = hashlib.sha256()
        with source_iso.open('rb') as src_stream:
            src_stream.seek(entry.extent * SECTOR)
            rem = entry.size
            while rem:
                blk = src_stream.read(min(rem, 4 * 1024 * 1024))
                if not blk:
                    break
                orig_digest.update(blk)
                rem -= len(blk)
        if orig_digest.hexdigest() != item['original_sha256']:
            raise ValueError(f'A ISO-base não corresponde ao vídeo original: {path}')
        if item.get('validation', {}).get('audio_unchanged') is not True or item.get('validation', {}).get('frames_equal') is not True:
            raise ValueError(f'Vídeo sem validação de áudio e quadros: {path}')
        result.append({'iso_path': str(path), 'payload': payload, 'sha256': item['sha256']})
    return result


def apply_movie_pack(output_iso: Path, movies: list[dict]) -> list[dict]:
    report = []
    for movie in movies:
        entry = find(output_iso, movie['iso_path'])
        payload = movie['payload']
        if len(payload) > entry.size:
            raise ValueError(f'Vídeo excede capacidade da ISO: {entry.path}')
        with output_iso.open('r+b') as stream:
            stream.seek(entry.extent * SECTOR)
            stream.write(payload)
            remaining = entry.size - len(payload)
            while remaining:
                block = bytes(min(remaining, 1024 * 1024))
                stream.write(block)
                remaining -= len(block)
        move_iso_file_record(output_iso, entry, entry.extent, len(payload))
        reopened_entry = find(output_iso, entry.path)
        digest = hashlib.sha256()
        with output_iso.open('rb') as stream:
            stream.seek(reopened_entry.extent * SECTOR)
            remaining = reopened_entry.size
            while remaining:
                chunk = stream.read(min(remaining, 4 * 1024 * 1024))
                if not chunk:
                    break
                digest.update(chunk)
                remaining -= len(chunk)
        if digest.hexdigest() != movie['sha256']:
            raise ValueError(f'Falha ao reabrir o vídeo inserido: {entry.path}')
        report.append({'iso_path': entry.path, 'bytes': len(payload), 'sha256': movie['sha256'], 'reopened_verified': True})
    return report
