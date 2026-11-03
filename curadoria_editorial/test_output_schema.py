import json

data = json.load(open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_030_output.json', encoding='utf-8'))
assert 'translations' in data, 'translations key missing'
assert 'dialogues' in data, 'dialogues key missing'
assert len(data['translations']) == 282, f"Expected 282 translations, got {len(data['translations'])}"
assert len(data['dialogues']) == 282, f"Expected 282 dialogues, got {len(data['dialogues'])}"

for t in data['translations']:
    assert 'id' in t, f"id missing in {t}"
    assert 'text' in t, f"text missing in {t}"
    assert '\r' not in t['text'], f"CR found in {t}"
    assert '\n.' not in t['text'], f"orphan . in {t}"
    assert '\n,' not in t['text'], f"orphan , in {t}"
    assert '\n...' not in t['text'], f"orphan ... in {t}"

print('Verificação da estrutura JSON: 100% CORRETA!')
