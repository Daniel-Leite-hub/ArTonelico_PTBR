from pathlib import Path
import sys,subprocess
root=Path(__file__).resolve().parents[1];sys.path.insert(0,str(root/'work/video_deps'))
import imageio_ffmpeg
from PIL import Image,ImageDraw
ff=imageio_ffmpeg.get_ffmpeg_exe();out=root/'Videos_editados_PTBR/auditoria/textos';out.mkdir(exist_ok=True)
paths=list((root/'Videos_originais_SFD/MOVIE/CSL').glob('*.SFD'))
for off in range(0,len(paths),6):
    page=Image.new('RGB',(1280,470),'black');draw=ImageDraw.Draw(page)
    for i,src in enumerate(paths[off:off+6]):
        dst=out/(src.stem+'.jpg')
        subprocess.run([ff,'-nostdin','-hide_banner','-loglevel','error','-n','-ss','12','-i',str(src),'-vf','scale=640:448,crop=640:120:0:300','-frames:v','1',str(dst)],capture_output=True)
        if dst.exists():page.paste(Image.open(dst),(i%2*640,i//2*155+25));draw.text((i%2*640,i//2*155),src.stem,fill='white')
    page.save(out/f'CSL_{off//6+1}.jpg')
