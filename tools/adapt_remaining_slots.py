"""Curated compact PT-BR; preserve master and full text, never mark approved."""
from pathlib import Path
import sys,json,sqlite3,re
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from artonelico_tool.patcher import selected_replacements,encode_game_text,build_iso
root=Path(__file__).resolve().parents[1]
adaptations={
8523816:'Choque forte',8523936:'Rejuvenescer',8524448:'Super Dive',8527104:'Golpe em elo',8527872:'Troca final',8533504:'Calmaria',8655360:'Moça F',8665200:'Dano de gelo',
8672000:'[Magia vermelha]CR10% do dano volta como MP.',8686752:'[Magia azul]CRAumenta bem a agilidade.',8787456:'Coroa real',8814344:'Gaiola de fumaça',8822304:'Desculpe, não posso comprar nada de você.',8824064:'Grato.',8833024:'Relevância ★★★CR【Canto】【Arte】',
8851584:'Eu não me preocupava, mas... Os níveis só subiam e entrei em pânico.',8917568:'Um dia, perguntei: “Como é o Lyner?”',8921568:'Que bom ouvir isso! Vamos seguir assim.',8964352:'Tudo bem. Vamos começar com... Krusche.',8970784:'Minha Cosmosfera era estranha. Devo ter te dado mais trabalho...',8974256:'É. A vida deles parece difícil. Mas tinham jardins e tal, então tudo bem.',9030152:'Mas estou feliz... Vou usar mais, até você se acostumar a me ver assim.',9049056:'Bem... foi difícil, sim. Mas foi divertido.',9102848:'Mas dá vergonha quando você me faz usar Magical Shower.',9179360:'Relaxe. Aonde você for, eu vou junto.',
9286152:'ELMA-DS4(Aurica)',9286200:'ELMA-DS4(Misha)',9339456:'O que foi?',9339480:'Faltam itens.',9340960:'Portão fechado.',9341816:'Quem deseja o cristal: mostre seu poder à porta.',9342704:'Veja bem, a parede aqui é nova...',9342920:'A parede foi reparada. Não parece quebrável.',9343040:'Há uma rachadura. Dá para quebrar?',9343128:'Quebrá-la pode abrir a porta.',9343840:'Porta bem pesada.',9343888:'Acesso bloqueado. Precisa de senha.',9344464:'Bloqueia a passagem. Vamos quebrá-la.',9345008:'Rotas: vermelho=fogo, azul=gelo, verde=vento, amarelo=raio.',
9345392:'Placa [Vermelha] vermelho→laranja→amarelo→verde→azul→magenta',9345512:'Placa [Laranja] vermelho→laranja→amarelo→verde→azul→magenta',9345640:'Placa [Amarela] vermelho→laranja→amarelo→verde→azul→magenta',9345768:'Placa [Verde] vermelho→laranja→amarelo→verde→azul→magenta',9345896:'Placa [Azul] vermelho→laranja→amarelo→verde→azul→magenta',9346024:'Placa [Magenta] vermelho→laranja→amarelo→verde→azul→magenta',9346152:'Vamos usar uma bomba elétrica para conduzir energia.',9346496:'Bomba elétrica pode conduzir energia.',9347320:'Não consigo passar aqui...',9347392:'Vamos à Floresta Viola recuperar a aeronave.',9347800:'Antes de seguir, vamos ver a aeronave no ponto de encontro.',9376328:'Após a tempestade, o tempo ficou lindo. Que sensação boa!',
9508976:'Personagem IM06 OKIM00 VoltarIM01',9509512:'CategoriaIM05 VoltarIM01',9511360:'Escolha alguém IM06 OKIM00 VoltarIM01',9511472:'Escolha quem trocar IM06 OKIM00 VoltarIM01',9511600:'Escolha Reyvateil IM06 OKIM00 VoltarIM01',9511712:'Magia de Canção IM06 OKIM00 VoltarIM01',9512224:'Usar em todos IM06 OKIM00 VoltarIM01',9512320:'Multiplicador IM05 OKIM00 VoltarIM01',9571840:'Pedra-canto',9598288:'Termos do mundo',9598392:'EscolherIM04 PáginaIM05 VoltarIM01',9598456:'EscolherIM04 MudarIM05 FimIM01',9621648:'[HP e MP restaurados!]',9623552:'LV1[Princesa Espinhosa]',9634864:'PáginaIM03 VoltarIM01',9638608:'EscolherIM04 TocarIM00 VoltarIM01',9639888:'EscolherIM04 FilmeIM00 VoltarIM01',9641832:'EscolherIM05 OcultarIM02 VoltarIM01',9651824:'Dive',9655808:'Tudo certo?',9656344:'Dive: Horai',9662184:'O que foi?',9662208:'Faltam itens.',9670912:'Dados danificados?',9671864:'Personagem IM06 OKIM00 VoltarIM01',9671944:'EquiparIM04 PersonagemIM05 OKIM00 VoltarIM01',9672192:'EscolherIM04 PersonagemIM05 OKIM00 VoltarIM01',9672544:'EquiparIM06 OKIM00 VoltarIM01',9672624:'NívelIM04 OKIM00 VoltarIM01',9672808:'Cristal GrathnodeIM06 OKIM00 VoltarIM01',9673400:'TrajeIM04 OKIM00 VoltarIM01',9673472:'PersonagemIM04 OKIM00 VoltarIM01',9673552:'Magia de CançãoIM04 OKIM00 VoltarIM01',9673632:'NívelIM04 Magia de CançãoIM05 OKIM00 VoltarIM01',9673744:'Cristal GrathnodeIM06 OKIM00 VoltarIM01',
9703488:'É, tem razão... Parece maligna e assustadora.',9719808:'Parece mais jaqueta que armadura, mas é resistente.',9724384:'E se tirar o bigode? Assim vira um terno normal.',9732120:'É fácil: faça um fio de Pelo Brilhante e esfregue a Asa de Dragão nele...',9737728:'E quando você tira?',9809920:'É preciso escolher: os efeitos ou seu pescoço.',9835104:'Cell... Lyner, isso já não foge do Grathmeld?',9840664:'O, o que há de errado?',9850880:'Este item faz você cantar mais rápido.',9870080:'O, o que quer dizer com monocromático?',9924624:'ItemIM06 OKIM00 VoltarIM01',9924752:'Cristal GrathnodeIM04 OKIM00 VoltarIM01',9924848:'QuantidadeIM05 OKIM00 VoltarIM01',9925008:'AvançarIM00 PularIM01',9925256:'Vendeu o antigo por %s Leaf. Agora: qualidade %s [%s] x%s.',9925512:'Posso chamá-lo de %s?',9925576:'ItemIM06 OKIM00',9925656:'QuantidadeIM05 OKIM00',9925712:'Cristal GrathnodeIM04 OKIM00',9928424:'Personagem IM06 OKIM00 VoltarIM01',9929984:'Vê o desenho nas minhas costas? O círculo no meio é minha porta de instalação.',10033488:'Compra',
}
adaptations.update({8523816:'Choque',8524448:'Mergulhão',8527104:'Golpe elo',
    8814344:'Gaiola fumosa',8833024:'Valor ★★★CR【Canto】【Arte】',
    9286152:'ELMA-DS4(Aur.)',9345392:'Placa[Vermelha] vermelho→laranja→amarelo→verde→azul→magenta',
    9598392:'EscolhaIM04 Pág.IM05 VoltaIM01',9638608:'EscolhaIM04 TocarIM00 VoltaIM01',
    9639888:'EscolhaIM04 FilmeIM00 VoltaIM01',9651824:'Mergul.',9656344:'Mergulho: Horai',
    9870080:'O, como assim, monocromático?',10033488:'Cp.'})

if __name__=='__main__':
    import shutil
    src=root/'release/ArTonelico_PTBR.atproj'
    dst=root/'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
    report=json.loads((root/'testes pt br/Ar tonelico PTBR pendentes banco adicional v2 20260926.capacity_fallbacks.json').read_text(encoding='utf8'))
    assert set(adaptations)=={r['entry_index'] for r in report}
    db=sqlite3.connect(src);db.row_factory=sqlite3.Row
    problems=[]
    for r in report:
        text=adaptations[r['entry_index']]
        row=db.execute('SELECT * FROM dialogues WHERE event_file=? AND entry_index=?',(r['event_file'],r['entry_index'])).fetchone()
        # Menu encoding does not use the dialogue accent escape.
        from artonelico_tool.native_menu_font import native_menu_text
        from artonelico_tool.patcher import MENU_RENDERER_GROUPS
        value=native_menu_text(text) if row['translation_track']=='localization' or r['event_file'] in MENU_RENDERER_GROUPS else text
        size=len(encode_game_text(value))
        if size>r['original_bytes']:problems.append((r['entry_index'],size,r['original_bytes'],text))
        assert re.findall(r'%s|IM\d\d|CR',text)==re.findall(r'%s|IM\d\d|CR',r['original']), (r['entry_index'],'commands')
        assert not row['reviewed'].strip(), 'Do not replace user review'
    if problems:print(json.dumps(problems,ensure_ascii=True,indent=2));sys.exit(1)
    if '--check' in sys.argv:print('108 adaptations fit; command tokens retained; master unchanged');sys.exit(0)
    if dst.exists():raise ValueError('Existing adapted project preserved')
    target=sqlite3.connect(dst);db.backup(target);target.row_factory=sqlite3.Row
    target.execute('CREATE TABLE compact_text_archive(event_file TEXT, entry_index INTEGER, full_automatic TEXT, full_translation TEXT, full_provider TEXT, compact_text TEXT, PRIMARY KEY(event_file,entry_index))')
    for r in report:
        key=(r['event_file'],r['entry_index']);text=adaptations[r['entry_index']]
        row=target.execute('SELECT * FROM dialogues WHERE event_file=? AND entry_index=?',key).fetchone()
        target.execute('INSERT INTO compact_text_archive VALUES(?,?,?,?,?,?)',(*key,row['automatic'],row['translation'],row['provider'],text))
        target.execute("UPDATE dialogues SET automatic=?,translation=?,translated_bytes=?,provider='local-adaptation',size_ok=1,error='' WHERE event_file=? AND entry_index=?",(text,text,len(encode_game_text(text)),*key))
    target.commit();target.close();db.close()
    result=build_iso(dst,root/'testes pt br/Ar tonelico PTBR adaptados 108 20260926.iso','native-menu-font',relocate=True,relocate_strings=True,expand_text_arena=True)
    print(json.dumps({k:v for k,v in result.items() if k!='capacity_fallbacks'},ensure_ascii=True,indent=2))
