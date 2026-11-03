"""Experimental extra PT_LOAD, with kernel heap AND libc sbrk reservation.

No runtime safety guarantee: reduced heap requires clean-boot/battle/scene QA.
Never overwrite BSS or reuse arbitrary zero-filled caves.
"""
import struct

OLD_END = 0xD44AFA
HEAP_POINTER = 0x746C64  # used by sbrk at VA 0x345428/2C/40
HEAP_HI = 0x11E4
HEAP_LO = 0x11EC
MAX_RESERVE = 1024*1024


def arena_layout(original):
    if original[:6] != b'\x7fELF\x01\x01':
        raise ValueError('Esperado ELF32 little-endian')
    phoff = struct.unpack_from('<I',original,28)[0]
    phsize,count = struct.unpack_from('<HH',original,42)
    if (phoff,phsize,count) != (52,32,1):
        raise ValueError('Layout ELF não aprovado para o banco adicional')
    load=struct.unpack_from('<8I',original,phoff)
    if load[0]!=1 or load[2]+load[5] != OLD_END:
        raise ValueError('Limite BSS diferente do executável investigado')
    if any(original[phoff+32:phoff+64]):
        raise ValueError('Cabeçalho adicional sobreporia dados existentes')
    guards={HEAP_HI:0x3C0400D4,HEAP_LO:0x24844AFA,HEAP_POINTER:OLD_END,
            0x11F4:0x2403003D,0x11F8:0x0000000C,
            0x1134:0x3C0300D4,0x113C:0x24634AFA,
            0x246428:0x8E425C64,0x24642C:0x8E425C64}
    for offset,value in guards.items():
        if struct.unpack_from('<I',original,offset)[0]!=value:
            raise ValueError(f'Inicialização/allocator não corresponde em {offset:#x}')
    return (len(original)+4095)&~4095, (OLD_END+4095)&~4095


def install_arena(executable, original, moves):
    offset,address = arena_layout(original)
    if not moves:
        return {}
    if any(m.destination < offset for m in moves):
        raise ValueError('Destino fora do banco adicional')
    size=max(m.destination+len(m.payload) for m in moves)-offset
    size=(size+4095)&~4095
    new_heap=address+size
    if new_heap-OLD_END > MAX_RESERVE:
        raise ValueError('Banco excede a reserva experimental de 1 MiB; não gerar')
    if len(executable)!=len(original):
        raise ValueError('Executável já expandido')
    for pos in (HEAP_HI,HEAP_LO,HEAP_POINTER):
        if executable[pos:pos+4]!=original[pos:pos+4]:
            raise ValueError('Inicialização de memória já foi alterada')
    executable.extend(b'\0'*(offset+size-len(executable)))
    struct.pack_into('<8I',executable,84,1,offset,address,address,size,size,4,4096)
    struct.pack_into('<H',executable,44,2)
    # BSS zeroing remains at OLD_END, otherwise it would erase the new text!
    struct.pack_into('<I',executable,HEAP_HI,0x3C040000|((new_heap+0x8000)>>16))
    struct.pack_into('<I',executable,HEAP_LO,0x24840000|(new_heap&0xFFFF))
    struct.pack_into('<I',executable,HEAP_POINTER,new_heap)
    return {'file_offset':offset,'virtual_address':address,'capacity_bytes':size,
            'heap_old_start':OLD_END,'heap_new_start':new_heap,
            'heap_reserved_bytes':new_heap-OLD_END,'experimental':True,
            'original_slots_preserved':True,'runtime_validated':False,
            'instruction_reference_paths_may_still_use_original':True}
