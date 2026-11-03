"""Extract original SFD files verbatim; never overwrite existing output."""
from pathlib import Path
import hashlib,json,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from artonelico_tool.iso import list_files,SECTOR

root=Path(__file__).resolve().parents[1]
iso=root/'Ar tonelico - Melody of Elemia (Undub).iso'
output=root/'Videos_originais_SFD'
if output.exists():
    raise FileExistsError(f'Pasta existente preservada: {output}')
entries=[e for e in list_files(iso) if not e.is_dir and e.path.startswith('MOVIE/') and e.path.upper().endswith('.SFD')]
if not entries:
    raise ValueError('Nenhum vídeo encontrado')
output.mkdir()
records=[]
with iso.open('rb') as source:
    for entry in entries:
        target=output/entry.path
        target.parent.mkdir(parents=True,exist_ok=True)
        source.seek(entry.extent*SECTOR)
        digest=hashlib.sha256()
        remaining=entry.size
        with target.open('xb') as dest:
            while remaining:
                block=source.read(min(1024*1024,remaining))
                if not block:raise EOFError(entry.path)
                dest.write(block);digest.update(block);remaining-=len(block)
        check=hashlib.sha256()
        with target.open('rb') as copied:
            while block:=copied.read(1024*1024):check.update(block)
        assert target.stat().st_size==entry.size and check.digest()==digest.digest(),entry.path
        records.append({'path':entry.path,'bytes':entry.size,'iso_lba':entry.extent,'sha256':digest.hexdigest()})
        print(f'{len(records)}/{len(entries)} {entry.path}',flush=True)
manifest={'source_iso':str(iso),'count':len(records),'total_bytes':sum(r['bytes'] for r in records),'verification':'size and SHA256 matched source bytes for every file','files':records}
with (output/'manifesto.json').open('x',encoding='utf8') as dest:
    json.dump(manifest,dest,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in manifest.items() if k!='files'},ensure_ascii=False))
