# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.project import encoded_size
print('A:', encoded_size('A'))
print('a:', encoded_size('a'))
print('space:', encoded_size(' '))
print('CR:', encoded_size('CR'))
print('ã:', encoded_size('ã'))
print('exclamation:', encoded_size('!'))
print('quote straight:', encoded_size('"'))
print('quote curly:', encoded_size('“'))
