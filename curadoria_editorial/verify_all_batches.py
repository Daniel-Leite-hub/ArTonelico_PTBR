# -*- coding: utf-8 -*-
import json
import re

from test_batch1 import batch1
from test_batch2 import batch2
from test_batch3 import batch3
from test_batch4 import batch4

all_lines = batch1 + batch2 + batch3 + batch4

print(f"Total curated lines: {len(all_lines)}")

# 1. Contiguity check
ids = [x['id'] for x in all_lines]
expected_ids = list(range(1888, 2115))
assert ids == expected_ids, f"IDs mismatch! Missing: {set(expected_ids) - set(ids)}"
print("Contiguity check passed: exactly IDs 1888 to 2114.")

# 2. Key completeness check
required_keys = ['id', 'file', 'speaker', 'original_jp', 'original_en', 'texto_ptbr_anterior', 'texto_ptbr_curado', 'status', 'justificativa']
for item in all_lines:
    for k in required_keys:
        assert k in item, f"Missing key {k} in item {item['id']}"
    assert item['status'] in ('rewritten', 'approved_as_is'), f"Invalid status {item['status']} in item {item['id']}"
    assert len(item['texto_ptbr_curado'].strip()) > 0, f"Empty text in item {item['id']}"
    assert len(item['justificativa'].strip()) > 0, f"Empty justificativa in item {item['id']}"
print("Key completeness check passed.")

# 3. Status count
rewritten = sum(1 for x in all_lines if x['status'] == 'rewritten')
approved = sum(1 for x in all_lines if x['status'] == 'approved_as_is')
print(f"Rewritten: {rewritten}, Approved as is: {approved}, Total: {len(all_lines)}")

# 4. Rubricas check
rubrica_pattern = re.compile(r'(\*[\w\s]+\*|\(.*suspiro.*\)|\(.*risos.*\)|Suspiro\.\.\.)', re.IGNORECASE)
for item in all_lines:
    m = rubrica_pattern.search(item['texto_ptbr_curado'])
    if m:
        print(f"[ERRO RUBRICA] ID {item['id']}: {m.group(0)} in '{item['texto_ptbr_curado']}'")
print("Rubrica check finished.")

# 5. Token shielding check
# Check for tokens in original: '#0', '[○○○]', '○', '%s', '%d', 'IM03', etc.
for item in all_lines:
    t = item['texto_ptbr_curado']
    # Check #0
    if '#0' in item['original_jp'] or '#0' in item['original_en']:
        assert '#0' in t, f"[ERRO TOKEN #0] ID {item['id']}: missing #0"
    # Check [○○○]
    if '○○○' in item['original_jp']:
        assert '○○○' in t, f"[ERRO TOKEN ○○○] ID {item['id']}: missing ○○○"
    # Check \r
    assert '\r' not in t, f"[ERRO \\r] ID {item['id']} contains \\r"

print("Token shielding check passed.")
