# -*- coding: utf-8 -*-
import json

gloss = json.load(open('G:/JOGO/PS2/Ar tonelico - Melody of Elemia (Undub)/Ferramentas_Traducao/curadoria_editorial/glossario_consulta.json', encoding='utf-8'))
for k, v in gloss.get('terms', {}).items():
    if 'Tastiella' in k or 'タスティエーラ' in str(v):
        print('Term:', k, v)
for k, v in gloss.get('characters', {}).items():
    if 'Tastiella' in k or 'タスティエーラ' in str(v):
        print('Char:', k, v)
