import glob, json

for f in sorted(glob.glob('Ferramentas_Traducao/curadoria_editorial/blocos/*output.json'))[-5:]:
    with open(f, 'r', encoding='utf-8') as fl:
        d = json.load(fl)
    inp_f = f.replace('_output.json', '_input.json')
    with open(inp_f, 'r', encoding='utf-8') as fl2:
        d_inp = json.load(fl2)
    diffs = 0
    for l_out, l_in in zip(d.get('dialogues', []), d_inp.get('dialogues', [])):
        if l_out.get('speaker') != l_in.get('speaker'):
            diffs += 1
            print(f"Diff in {f}: in={l_in.get('speaker')} -> out={l_out.get('speaker')}")
            break
    if diffs == 0:
        print(f"{f}: all speakers identical to input")
