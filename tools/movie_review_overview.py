from pathlib import Path
import sys,subprocess
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'work/video_deps'))
import imageio_ffmpeg
from PIL import Image,ImageDraw
ff=imageio_ffmpeg.get_ffmpeg_exe();out=root/'Videos_editados_PTBR/auditoria/overview';out.mkdir(exist_ok=True)
sources=list((root/'Videos_originais_SFD/MOVIE').rglob('*.SFD'))
groups={name:[p for p in sources if p.parent.name==name] for name in ('CS','CSL','EVENT','OP','ED')}
for group,paths in groups.items():
    for offset in range(0,len(paths),6):
        page=Image.new('RGB',(1280,750),'black');draw=ImageDraw.Draw(page)
        for index,src in enumerate(paths[offset:offset+6]):
            dst=out/f'{group}_{src.stem}.jpg'
            if not dst.exists():
                subprocess.run([ff,'-nostdin','-hide_banner','-loglevel','error','-n','-ss','8','-i',str(src),'-frames:v','1','-q:v','2',str(dst)],capture_output=True)
            if dst.exists():
                im=Image.open(dst);im.thumbnail((640,224));x=index%2*640;y=index//2*250;page.paste(im,(x,y+23));draw.text((x+5,y+3),src.relative_to(root/'Videos_originais_SFD').as_posix(),fill='white')
        page.save(out/f'{group}_page{offset//6+1}.jpg')
sys.stdout.reconfigure(encoding='utf8')
db=__import__('sqlite3').connect(root/'release/ArTonelico_PTBR_adaptado_108_20260926.atproj')
for original,automatic in db.execute("SELECT original,automatic FROM dialogues WHERE original LIKE '%Blastline%' LIMIT 12"):
    print(original,automatic)
for row in db.execute("SELECT original,automatic FROM dialogues WHERE original IN ('Magical Shuttle','Sheep Sweets','Sailor Girl','Y','SHINOBI','KASHA','White Kimono','Elfir','China Dress','Skuywat','Holy Guard','School Days','Don Leon','Bubble Passion','SERAPH','LILIM','Ceremony','Marlone') OR original LIKE 'Magical S%' OR original LIKE 'Sheep S%' OR original LIKE 'Skyw%' OR original LIKE 'Marlo%' OR original LIKE 'Sailor %'"):
    print(row)
