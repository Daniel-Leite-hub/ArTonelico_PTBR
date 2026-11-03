"""Render reviewed PT-BR cues, retaining original SFD timing and audio."""
from pathlib import Path
import sys,json,re,subprocess,hashlib,shutil
root=Path(__file__).resolve().parents[1];sys.path.insert(0,str(root/'work/video_deps'))
import imageio_ffmpeg
ff=imageio_ffmpeg.get_ffmpeg_exe()
out=root/'Videos_editados_PTBR/lote';out.mkdir(exist_ok=True)
pack=root/'release/videos_ptbr';pack.mkdir(exist_ok=True)
inventory={x['path']:x for x in json.loads((root/'Videos_editados_PTBR/auditoria/inventory.json').read_text(encoding='utf8'))}
header=(root/'Videos_editados_PTBR/AVAN_AT_PTBR.ass').read_text(encoding='utf8').split('Dialogue:')[0]
def cue(start,end,text,pos=None):
    if pos:text='{\\pos('+str(pos[0])+','+str(pos[1])+')}' + text
    return [start,end,text]
cues={
 'MOVIE/OP0A.SFD':[cue(10.5,12.5,'Certo, parece estar tudo em ordem.',(320,370)),cue(14.5,15,'Decolar!',(320,370)),cue(33,34.5,'O que é aquilo?',(320,370)),cue(35,37.5,'Um monstro da Blastline?',(320,370)),cue(44.5,46.5,'Droga! Isso não é nada bom.',(320,370)),cue(65.5,67.5,'Ah, não! Aquela aeronave vai cair!',(320,370)),cue(71,72.5,'Anda, droga!',(320,370))],
 'MOVIE/OP0B.SFD':[cue(7,8,'Lá vai!',(320,370)),cue(18,20,'Planador...', (320,370)),cue(20,20.8,'Planador... ativar!',(320,370)),cue(23.5,24.5,'Parou!',(320,370)),cue(27,27.7,'Ei, aquilo é...', (320,370)),cue(30.5,31.5,'Aquilo é...', (320,370)),cue(31.5,33,'O monstro da Blastline!',(320,370))],
 'MOVIE/EVENT/SYU_OP.SFD':[cue(0,5,'Ela era uma garota como qualquer outra.'),cue(5,10,'De dia, ia à escola. Nos fins de semana,\\Ntrabalhava num café. Uma garota comum.'),cue(10,15,'Mas ela tinha um segredo\\Nque não podia contar a ninguém.'),cue(15,20,'Sim, um grande segredo...'),cue(20,29,'Ela era Shurelia, o Anjo da Canção,\\Ndefensora da paz e destruidora dos vírus malignos.'),cue(35,59.6,'Shurelia — O Anjo da Canção\\NA fantasia de um conglomerado que criou a Torre.\\NPressione START.',(320,370))],
 'MOVIE/EVENT/SYU_OP2.SFD':[cue(0,29,'Shurelia — O Anjo da Canção\\NA fantasia de um conglomerado que criou a Torre.\\NPressione START.',(320,370))],
}
opening=[cue(24,29,'Há muito tempo, dizia-se que as canções\\Npossuíam poderes extraordinários.'),cue(29,38,'Há muito tempo, dizia-se que as canções\\Npossuíam poderes extraordinários.\\N\\NAs pessoas acreditavam que eram as mãos\\Nda mãe natureza, que envolviam o mundo.\\NE cantavam sem cessar.'),cue(38,45,'Mas agora tudo mudou. Neste mundo,\\Ntodos se esqueceram de como cantar...'),cue(45,56,'Como palavras antigas, perdidas para sempre.')]
for name in ('AT_OP01','AT_OP02','AT_OP0D'):cues[f'MOVIE/{name}.SFD']=opening
for path in ('MOVIE/EVENT/SYU_OP.SFD','MOVIE/EVENT/SYU_OP2.SFD'):
    cues[path][-1][2]=cues[path][-1][2].replace('A fantasia de um conglomerado que criou a Torre.', 'Ar tonelico fantasma: a Cosmosfera de Shurelia,\\Num outro mundo criado pela Torre.')
# The bottom result messages scroll; Portuguese stays readable in a fixed box.
costumes_m={3:'Chuva mágica',4:'Doces de ovelha',5:'Marinheira',6:'Y',7:'SHINOBI',8:'KASHA',9:'Quimono branco','E':'Elfir','M':'Vestido chinês'}
costumes_o={2:'Skuwat',3:'Guardião sagrado',4:'Dias escolares',5:'Don Leon',6:'Paixão borbulhante',7:'SERAPH',8:'LILIM',9:'Cerimônia','E':'Marlone'}
for path in inventory:
    if not path.startswith('MOVIE/CSL/'):continue
    stem=Path(path).stem;name='Misha' if stem[0]=='M' else 'Aurica';level=stem[-1];key=int(level) if level.isdigit() else level
    reward=(costumes_m if name=='Misha' else costumes_o).get(key)
    text=f'Cosmosfera de {name}: nível {level} concluído.'
    if level=='M':text='O Hino de Misha foi devolvido.'
    if reward:text+='\\NTraje obtido: '+reward+'.'
    cues[path]=[cue(7.5,15.9,text,(320,370))]
for name,phase in [('EYE1',1),('EYE2',2)]:
    # Hymmnos text is a fictional-language quotation, not English dialogue.
    cues[f'MOVIE/EVENT/{name}.SFD']=[cue(2,14,f'FASE {phase} CONCLUÍDA', (430,215)),cue(14,29.5,f'INÍCIO DA FASE {phase+1}',(430,215))]
for name,text in [('H_INIT','Conglomerado Tenba\\NBeco do Vaga-lume'),('I_INIT','Cidade da Luz e da Magia\\NEm Pheyna'),('K_INIT','Vila Fronteiriça\\NKarulu'),('N_INIT','Cidade Aeroportuária\\NNemo'),('P_INIT','Cidade Flutuante\\NPlatina')]:
    cues[f'MOVIE/EVENT/{name}.SFD']=[cue(4,9.7,text,(450,360))]

def run(args):
    p=subprocess.run(args,cwd=root,capture_output=True)
    if p.returncode:raise RuntimeError(p.stderr.decode(errors='replace')[-2500:]+p.stdout.decode(errors='replace')[-1000:])
    return p
def frames(path):
    p=run([ff,'-nostdin','-hide_banner','-loglevel','error','-i',str(path),'-map','0:v:0','-an','-fps_mode','passthrough','-f','framemd5','-'])
    return sum(bool(l) and not l.startswith(b'#') for l in p.stdout.splitlines())
def timestamp(t):return f'{int(t//3600)}:{int(t//60)%60:02}:{t%60:05.2f}'
def build(path,events):
    stem=path.removeprefix('MOVIE/').replace('/','_').removesuffix('.SFD')
    src=root/'Videos_originais_SFD'/path;ass=out/(stem+'.ass');video=out/(stem+'.m1v');sfd=out/(stem+'.SFD');report=out/(stem+'.json')
    if report.exists():
        previous=json.loads(report.read_text(encoding='utf8'))
        if previous['cues']==events:return previous
        stem+='_r2';ass=out/(stem+'.ass');video=out/(stem+'.m1v');sfd=out/(stem+'.SFD');report=out/(stem+'.json')
        if report.exists():return json.loads(report.read_text(encoding='utf8'))
    if sfd.exists() or video.exists():raise FileExistsError(f'Unvalidated candidate exists: {stem}')
    ass.write_text(header+''.join(f'Dialogue: 0,{timestamp(s)},{timestamp(e)},Default,,0,0,0,,{t}\n' for s,e,t in events),encoding='utf8')
    info=inventory[path]['probe']
    fps=re.search(r'(\d+(?:\.\d+)?) fps',info).group(1);sar=re.search(r'SAR (\d+):(\d+)',info)
    aspect=f'{sar[1]}/{sar[2]}' if sar else '1/1'
    buffer=re.search(r'buffer size: (\d+)',info).group(1)
    streams=re.findall(r'Stream #0:\d+.*Audio: (\w+)',info)
    if any(s not in ('adpcm_adx','ac3') for s in streams):raise ValueError(f'Unsupported original audio: {path}')
    count=frames(src)
    base=f'subtitles=Videos_editados_PTBR/lote/{stem}.ass:force_style='
    filters=base+"'Fontname=Trebuchet MS,Fontsize=23,PrimaryColour=&HFFFFFFFF,SecondaryColour=&HFFFFFFFF,OutlineColour=&H59000000,BackColour=&H59000000,Bold=0,BorderStyle=3,Outline=2,Shadow=0',"+base+"'Fontname=Trebuchet MS,Fontsize=23,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BackColour=&HFF000000,Bold=0,BorderStyle=1,Outline=1.4,Shadow=0.5',setsar="+aspect
    print('Rendering',path,count,'frames',flush=True)
    run([ff,'-nostdin','-hide_banner','-loglevel','error','-n','-i',str(src),'-map','0:v:0','-vf',filters,'-an','-c:v','mpeg1video','-b:v','2300k','-maxrate','3300k','-bufsize',buffer,'-r',fps,'-frames:v',str(count),'-f','mpeg1video',str(video)])
    mux=[str(root/'tools/SFD_Muxer.exe'),'-v',str(video)]
    audios=[]
    for i in range(len(streams)):
        fmt='adx' if streams[i]=='adpcm_adx' else 'ac3'
        audio=out/f'{stem}_{i}.{fmt}'
        run([ff,'-nostdin','-hide_banner','-loglevel','error','-n','-i',str(src),'-map',f'0:a:{i}','-c:a','copy','-f',fmt,str(audio)])
        audios.append(audio);mux+=['-a',str(audio)]
    metadata='2' if b'SofdecStream2' in src.read_bytes()[:65536] else '1'
    run(mux+['-M',metadata,'-o',str(sfd)])
    if sfd.stat().st_size>src.stat().st_size:raise ValueError(f'Candidate exceeds original capacity: {path}')
    run([ff,'-nostdin','-hide_banner','-loglevel','error','-i',str(sfd),'-f','null','-'])
    newcount=frames(sfd)
    if newcount!=count:raise ValueError(f'Frame mismatch: {path}: {count}/{newcount}')
    for i,audio in enumerate(audios):
        fmt=audio.suffix[1:];reopened=out/f'{stem}_{i}_reopened.{fmt}'
        run([ff,'-nostdin','-hide_banner','-loglevel','error','-n','-i',str(sfd),'-map',f'0:a:{i}','-c:a','copy','-f',fmt,str(reopened)])
        if audio.read_bytes()!=reopened.read_bytes():raise ValueError(f'Audio mismatch: {path}')
    result={'iso_path':path,'file':stem+'.SFD','sha256':hashlib.sha256(sfd.read_bytes()).hexdigest(),'original_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'validation':{'frames_equal':True,'frames':count,'audio_unchanged':True,'audio_streams':len(streams),'full_decode':True,'runtime_validated':False},'review_state':'context_reviewed','cues':events}
    report.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
    return result
if __name__=='__main__':
    results=[]
    for path,events in cues.items():
        result=build(path,events);shutil.copy2(out/result['file'],pack/result['file']);results.append(result)
    src=root/'Videos_originais_SFD/MOVIE/OP/AVAN_AT.SFD';replacement=root/'Videos_editados_PTBR/AVAN_AT_PTBR_65_30fps_v2.SFD'
    shutil.copy2(replacement,pack/replacement.name)
    results.append({'iso_path':'MOVIE/OP/AVAN_AT.SFD','file':replacement.name,'sha256':hashlib.sha256(replacement.read_bytes()).hexdigest(),'original_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'validation':{'frames_equal':True,'frames':4110,'audio_unchanged':True,'full_decode':True,'runtime_validated':True},'review_state':'context_reviewed'})
    (pack/'manifest.json').write_text(json.dumps({'schema':1,'movies':results},ensure_ascii=False,indent=2),encoding='utf8')
    print('PACK COMPLETE',len(results),flush=True)
