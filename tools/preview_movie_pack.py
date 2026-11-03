from pathlib import Path
import sys,subprocess,json
root=Path(__file__).resolve().parents[1];sys.path.insert(0,str(root/'work/video_deps'))
import imageio_ffmpeg
from PIL import Image,ImageDraw
ff=imageio_ffmpeg.get_ffmpeg_exe();pack=root/'release/videos_ptbr';out=root/'Videos_editados_PTBR/auditoria/preview';out.mkdir(exist_ok=True)
manifest=json.loads((pack/'manifest.json').read_text(encoding='utf8'))['movies']
selected=[('MOVIE/OP0A.SFD',35.5),('MOVIE/OP0B.SFD',19),('MOVIE/AT_OP01.SFD',32),('MOVIE/EVENT/SYU_OP.SFD',23),('MOVIE/CSL/MLV5.SFD',12),('MOVIE/EVENT/I_INIT.SFD',5)]
page=Image.new('RGB',(1280,1410),'black');draw=ImageDraw.Draw(page)
for i,(path,t) in enumerate(selected):
    item=next(x for x in manifest if x['iso_path']==path);dst=out/(Path(item['file']).stem+'.jpg')
    subprocess.run([ff,'-nostdin','-hide_banner','-loglevel','error','-n','-ss',str(t),'-i',str(pack/item['file']),'-frames:v','1',str(dst)],check=True)
    page.paste(Image.open(dst),(i%2*640,i//2*470+22));draw.text((i%2*640+5,i//2*470+3),path,fill='white')
page.save(out/'lote_PTBR.jpg')
