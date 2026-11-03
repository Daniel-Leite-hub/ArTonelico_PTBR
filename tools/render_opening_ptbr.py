"""Editable preview and separate MPEG/ADX assets, not a game-ready SFD."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'work/video_deps'))
import imageio_ffmpeg
ff=imageio_ffmpeg.get_ffmpeg_exe()
src='Videos_originais_SFD/MOVIE/OP/AVAN_AT.SFD'
out='Videos_editados_PTBR/AVAN_AT_PTBR_previa_Trebuchet_fundo_65.mp4'
# Older previews remain intact for comparison.
# Rounded humanist letterforms, white foreground, outline only; no opaque box.
base="subtitles=Videos_editados_PTBR/AVAN_AT_PTBR.ass:force_style="
# Draw translucent line-sized boxes first, then the unchanged outlined letters.
filters=base+"'Fontname=Trebuchet MS,Fontsize=23,PrimaryColour=&HFFFFFFFF,SecondaryColour=&HFFFFFFFF,OutlineColour=&H59000000,BackColour=&H59000000,Bold=0,BorderStyle=3,Outline=2,Shadow=0',"+base+"'Fontname=Trebuchet MS,Fontsize=23,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BackColour=&HFF000000,Bold=0,BorderStyle=1,Outline=1.4,Shadow=0.5'"
def run(args):subprocess.run([ff,'-nostdin','-hide_banner','-loglevel','warning','-n',*args],cwd=root,check=True)
run(['-i',src,'-map','0:v:0','-map','0:a:0','-vf',filters,'-c:v','libx264','-crf','16','-preset','medium','-c:a','aac','-b:a','192k','-movflags','+faststart',out])
if not (root/'Videos_editados_PTBR/AVAN_AT_audio_original.adx').exists():
    run(['-i',src,'-map','0:a:0','-c:a','copy','-f','adx','Videos_editados_PTBR/AVAN_AT_audio_original.adx'])
run(['-i',src,'-map','0:v:0','-vf',filters,'-an','-c:v','mpeg1video','-b:v','3000k','-maxrate','4000k','-bufsize','1835008','-r','24','-f','mpeg1video','Videos_editados_PTBR/AVAN_AT_PTBR_Trebuchet_fundo_65.m1v'])
run(['-i',out,'-vf','fps=1/12,scale=320:224,tile=4x3','-frames:v','1','Videos_editados_PTBR/AVAN_AT_PTBR_Trebuchet_fundo_65_contato.png'])
run(['-i',out,'-map','0:v:0','-map','0:a:0','-f','null','-'])
print('Preview fully decoded; original ADX copied; edited MPEG-1 retained. NOT a rebuilt or runtime-validated SFD.')
