import json, sqlite3, sys
from pathlib import Path
sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.project import encoded_size

cfg = json.load(open('Ferramentas_Traducao/curadoria_editorial/curadoria_config.json', 'r', encoding='utf-8'))
conn = sqlite3.connect(cfg['database_path'])
c = conn.cursor()
caps = {row[0]: row[1] for row in c.execute('SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 32421 AND 32708').fetchall()}
conn.close()

data = json.load(open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_043_input.json', 'r', encoding='utf-8'))
dialogues = {d['id']: d for d in data['dialogues']}

def dump_range(start_id, end_id, outfile):
    with open(outfile, 'w', encoding='utf-8') as out:
        for did in range(start_id, end_id + 1):
            d = dialogues[did]
            cap = caps[did]
            cur = d.get('current_ptbr', '')
            sz = encoded_size(cur)
            out.write(f'=== ID {did} | CAP: {cap}B | CUR: {sz}B | OVER: {sz - cap}B | FILE: {d.get("event_file")} ===\n')
            out.write(f'JP: {d.get("original_jp")}\n')
            out.write(f'EN: {d.get("original_en")}\n')
            out.write(f'PT: {cur}\n\n')

if __name__ == '__main__':
    part = sys.argv[1]
    if part == '1':
        dump_range(32421, 32516, 'Ferramentas_Traducao/curadoria_editorial/part1_dump.txt')
    elif part == '2':
        dump_range(32517, 32612, 'Ferramentas_Traducao/curadoria_editorial/part2_dump.txt')
    elif part == '3':
        dump_range(32613, 32708, 'Ferramentas_Traducao/curadoria_editorial/part3_dump.txt')
