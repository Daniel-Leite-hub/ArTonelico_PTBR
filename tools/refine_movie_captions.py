from pathlib import Path
import sys,subprocess,json
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'work/video_deps'))
import imageio_ffmpeg
ff=imageio_ffmpeg.get_ffmpeg_exe()
inventory=json.loads((root/'Videos_editados_PTBR/auditoria/inventory.json').read_text(encoding='utf8'))
out=root/'Videos_editados_PTBR/auditoria/detalhes';out.mkdir(exist_ok=True)
for item in inventory:
    if item['path'] not in ('MOVIE/OP0A.SFD','MOVIE/OP0B.SFD','MOVIE/AT_OP01.SFD'):continue
    src=root/'Videos_originais_SFD'/item['path'];stem=src.stem
    subprocess.run([ff,'-nostdin','-hide_banner','-loglevel','error','-n','-i',str(src),'-vf','fps=2,crop=640:140:0:300,scale=480:105,tile=3x10','-fps_mode','passthrough','-q:v','2',str(out/f'{stem}_%02d.jpg')],check=True)
    print(item['path'],item['probe'],flush=True)
