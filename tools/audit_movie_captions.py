"""Contact sheets for every original SFD; this is sampling, not full subtitle QA."""
from pathlib import Path
import sys,json,subprocess,concurrent.futures
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'work/video_deps'))
import imageio_ffmpeg
ff=imageio_ffmpeg.get_ffmpeg_exe()
out=root/'Videos_editados_PTBR/auditoria'
out.mkdir(exist_ok=True)
entries=json.loads((root/'Videos_originais_SFD/manifesto.json').read_text(encoding='utf8'))['files']
def inspect(entry):
    src=root/'Videos_originais_SFD'/entry['path']
    stem=entry['path'].removeprefix('MOVIE/').replace('/','_').removesuffix('.SFD')
    dst=out/f'{stem}_%02d.jpg'
    info=subprocess.run([ff,'-hide_banner','-i',str(src)],capture_output=True).stderr.decode(errors='replace')
    if not list(out.glob(stem+'_*.jpg')):
        process=subprocess.run([ff,'-nostdin','-hide_banner','-loglevel','error','-threads','2','-i',str(src),'-vf','fps=1/5,scale=320:224,tile=4x4','-fps_mode','passthrough','-q:v','3',str(dst)],capture_output=True)
        if process.returncode:
            return {'path':entry['path'],'probe':info,'sheets':[],'error':process.stderr.decode(errors='replace')}
    return {'path':entry['path'],'probe':info,'sheets':[p.name for p in sorted(out.glob(stem+'_*.jpg'))]}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    results=[]
    for result in pool.map(inspect,entries):
        results.append(result);print(f"{len(results)}/102 {result['path']}",flush=True)
(out/'inventory.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
