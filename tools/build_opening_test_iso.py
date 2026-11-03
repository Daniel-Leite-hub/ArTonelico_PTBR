"""Create experimental ISO with localized SFD; preserve all input artifacts."""
from pathlib import Path
import sys,subprocess,json,hashlib
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from artonelico_tool.patcher import build_iso
from artonelico_tool.iso import find,read_entry,SECTOR
from artonelico_tool.relocation import move_iso_file_record
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'work/video_deps'))
import imageio_ffmpeg
ff=imageio_ffmpeg.get_ffmpeg_exe()
directory=root/'Videos_editados_PTBR'
src=root/'Videos_originais_SFD/MOVIE/OP/AVAN_AT.SFD'
video=directory/'AVAN_AT_PTBR_65_30fps_v2.m1v'
sfd=directory/'AVAN_AT_PTBR_65_30fps_v2.SFD'
audio=directory/'AVAN_AT_audio_original.adx'
iso=root/'testes pt br/Ar tonelico PTBR abertura 65 teste 20260926.iso'
if any(p.exists() for p in (video,sfd,iso)):raise FileExistsError('Output already exists; preserve it')
base="subtitles=Videos_editados_PTBR/AVAN_AT_PTBR.ass:force_style="
filters=base+"'Fontname=Trebuchet MS,Fontsize=23,PrimaryColour=&HFFFFFFFF,SecondaryColour=&HFFFFFFFF,OutlineColour=&H59000000,BackColour=&H59000000,Bold=0,BorderStyle=3,Outline=2,Shadow=0',"+base+"'Fontname=Trebuchet MS,Fontsize=23,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BackColour=&HFF000000,Bold=0,BorderStyle=1,Outline=1.4,Shadow=0.5',setsar=200/219"
def run(args):return subprocess.run(args,cwd=root,check=True,capture_output=True)
print('Encode MPEG-1, original 30fps / 640x448',flush=True)
run([ff,'-nostdin','-hide_banner','-loglevel','error','-n','-i',str(src),'-map','0:v:0','-vf',filters,'-an','-c:v','mpeg1video','-b:v','3000k','-maxrate','4000k','-bufsize','1179648','-r','30','-frames:v','4110','-f','mpeg1video',str(video)])
run([str(root/'tools/SFD_Muxer.exe'),'-v',str(video),'-a',str(audio),'-M','1','-o',str(sfd)])
print('Decode and audio verification',flush=True)
run([ff,'-nostdin','-hide_banner','-loglevel','error','-i',str(sfd),'-map','0:v:0','-map','0:a:0','-f','null','-'])
reopened=directory/'AVAN_AT_audio_30fps_v2_reaberto.adx'
run([ff,'-nostdin','-hide_banner','-loglevel','error','-n','-i',str(sfd),'-map','0:a:0','-c:a','copy','-f','adx',str(reopened)])
assert audio.read_bytes()==reopened.read_bytes(),'Audio stream changed'
frames=[]
for source in (src,sfd):
    result=run([ff,'-nostdin','-hide_banner','-loglevel','error','-i',str(source),'-map','0:v:0','-an','-fps_mode','passthrough','-f','framemd5','-'])
    count=sum(1 for line in result.stdout.splitlines() if line and not line.startswith(b'#'))
    frames.append(count)
assert frames[0]==frames[1],frames
print('Frames:',frames,flush=True)
entry=find(root/'Ar tonelico - Melody of Elemia (Undub).iso','MOVIE/OP/AVAN_AT.SFD')
payload=sfd.read_bytes()
assert len(payload)<=entry.size,'No relocation of movie permitted in this test'
print('Build translated ISO from updated project',flush=True)
result=build_iso(root/'release/ArTonelico_PTBR_adaptado_108_20260926.atproj',iso,'native-menu-font',relocate=True,relocate_strings=True,expand_text_arena=True)
entry=find(iso,entry.path)
with iso.open('r+b') as fp:
    fp.seek(entry.extent*SECTOR);fp.write(payload)
    remaining=entry.size-len(payload)
    while remaining:
        block=bytes(min(remaining,1024*1024));fp.write(block);remaining-=len(block)
move_iso_file_record(iso,entry,entry.extent,len(payload))
assert read_entry(iso,find(iso,entry.path))==payload
sha=hashlib.sha256()
with iso.open('rb') as fp:
    while block:=fp.read(8*1024*1024):sha.update(block)
report={k:v for k,v in result.items() if k!='capacity_fallbacks'}
report.update(output_sha256=sha.hexdigest(),movie_path=entry.path,movie_bytes=len(payload),original_frames=frames[0],new_frames=frames[1],audio_unchanged=True,movie_reopened_verified=True,runtime_validated=False)
with iso.with_suffix('.opening_audit.json').open('x',encoding='utf8') as fp:json.dump(report,fp,ensure_ascii=False,indent=2)
print(json.dumps(report,ensure_ascii=True,indent=2))
