"""Restrict instruction relocation to isolated adjacent LUI/ADDIU or ORI pairs."""
import struct
from dataclasses import dataclass


@dataclass(frozen=True)
class AddressPair:
    hi: int
    lo: int
    value: int
    ori: bool


def branch(word):
    op=word>>26
    return op in (1,2,3,4,5,6,7,20,21,22,23) or (op==0 and word&63 in (8,9)) or (op in (16,17,18) and (word>>21)&31==8)


def adjacent_address_pairs(data, sections):
    entry_targets=set()
    ranges=[(s[4],s[4]+s[5],s[3]-s[4]) for s in sections if s[2]&6==6 and s[1]!=8]
    for start,end,bias in ranges:
        for p in range(start,end-3,4):
            w=struct.unpack_from('<I',data,p)[0];op=w>>26;va=p+bias
            if op in (2,3):entry_targets.add(((va+4)&0xf0000000)|((w&0x3ffffff)<<2))
            elif branch(w) and op not in (0,2,3):
                low=w&65535;entry_targets.add(va+4+4*(low if low<32768 else low-65536))
    result={}
    for start,end,bias in ranges:
        for p in range(start,end-7,4):
            hi,lo=struct.unpack_from('<2I',data,p)
            if hi>>26!=15 or lo>>26 not in (9,13):continue
            reg=(hi>>16)&31
            if reg==0 or (lo>>21)&31!=reg or (lo>>16)&31!=reg:continue
            if p>start and branch(struct.unpack_from('<I',data,p-4)[0]):continue
            if p+4+bias in entry_targets:continue
            low=lo&65535;is_ori=lo>>26==13
            value=((hi&65535)<<16)|low if is_ori else ((hi&65535)<<16)+(low if low<32768 else low-65536)
            result.setdefault(value,[]).append(AddressPair(p,p+4,value,is_ori))
    return result


def rewrite_pair(data, pair, value):
    hi,lo=struct.unpack_from('<2I',data,pair.hi)
    reg=(hi>>16)&31
    low=lo&65535
    actual=((hi&65535)<<16)|low if pair.ori else ((hi&65535)<<16)+(low if low<32768 else low-65536)
    if actual!=pair.value or pair.lo!=pair.hi+4 or hi>>26!=15 or lo>>26!=(13 if pair.ori else 9) or (lo>>21)&31!=reg or (lo>>16)&31!=reg:
        raise ValueError('Par MIPS mudou antes da realocação')
    new_hi=(value>>16) if pair.ori else ((value+0x8000)>>16)
    struct.pack_into('<I',data,pair.hi,(hi&0xffff0000)|(new_hi&65535))
    struct.pack_into('<I',data,pair.lo,(lo&0xffff0000)|(value&65535))
