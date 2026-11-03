# -*- coding: utf-8 -*-
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, 'Ferramentas_Traducao')
sys.path.insert(0, 'Ferramentas_Traducao/tools')
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

DB_PATH = Path('Ferramentas_Traducao/ArTonelico_PTBR.atproj')

def check_curations(curation_dict, verbose=True):
    """
    curation_dict: dict of {dialogue_id: (curated_text, rationale)}
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    total = len(curation_dict)
    overflows = []
    val_errors = []
    
    for d_id, (text, rat) in sorted(curation_dict.items()):
        c.execute("SELECT original, original_jp, original_bytes FROM dialogues WHERE id = ?", (d_id,))
        row = c.fetchone()
        if not row:
            print(f"ERRO: ID {d_id} não encontrado no banco!")
            continue
        orig_en, orig_jp, cap = row[0], row[1], row[2]
        sz = encoded_size(text)
        
        # 1. Byte overflow check
        if sz > cap:
            overflows.append((d_id, cap, sz, sz - cap, text))
            
        # 2. Hard Gate validation check
        errs = validate_line(d_id, orig_en, text)
        if errs:
            val_errors.append((d_id, errs))
            
    conn.close()
    
    if verbose:
        print(f"Total avaliado: {total}")
        print(f"Estouros de buffer: {len(overflows)}")
        print(f"Erros de validação: {len(val_errors)}")
        
        if overflows:
            print("\n--- ESTOUROS DETECTADOS ---")
            for d_id, cap, sz, diff, txt in overflows:
                print(f"ID {d_id}: Cap {cap}B, Encoded {sz}B (+{diff}B) | {txt}")
                
        if val_errors:
            print("\n--- ERROS DE VALIDAÇÃO TÉCNICA ---")
            for d_id, errs in val_errors:
                print(f"ID {d_id}: {'; '.join(errs)}")
                
    return len(overflows) == 0 and len(val_errors) == 0

if __name__ == '__main__':
    print("Helper pronto.")
