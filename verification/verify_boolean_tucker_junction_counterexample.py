#!/usr/bin/env python3
"""Solver-free verification of the Boolean Tucker junction counterexample."""
from itertools import combinations_with_replacement, product

DIMS=(2,4,4)
BAD_WORD=0x3EEBE9BE
GOOD_WORD=0xEEE3113E
CHECKS=0

def require(c,m):
    global CHECKS
    CHECKS+=1
    if not c: raise RuntimeError('FAIL: '+m)

def tensor_from_word(word,dims):
    a,b,c=dims
    return frozenset((i,j,k) for i in range(a) for j in range(b) for k in range(c)
                     if (word>>((i*b+j)*c+k))&1)

def unfolding_columns(T,dims,mode):
    other=tuple(i for i in range(3) if i!=mode)
    cols=set()
    for opp in product(*(range(dims[i]) for i in other)):
        m=0
        for x in range(dims[mode]):
            p=[0,0,0]; p[mode]=x; p[other[0]],p[other[1]]=opp
            if tuple(p) in T: m|=1<<x
        cols.add(m)
    return frozenset(cols)

def intersection_generators(cols,dim):
    items=tuple(sorted(cols)); out=set()
    for sel in range(1,1<<len(items)):
        v=(1<<dim)-1
        for i,c in enumerate(items):
            if (sel>>i)&1: v&=c
        out.add(v)
    return tuple(sorted(out))

def union_closure(fam):
    out={0}
    for g in fam: out|={x|g for x in tuple(out)}
    return frozenset(out)

def exact_rank_and_families(cols,dim):
    gens=intersection_generators(cols,dim)
    for r in range(dim+1):
        fs=frozenset(f for f in combinations_with_replacement(gens,r) if cols<=union_closure(f))
        if fs: return r,fs
    raise RuntimeError('no factorization')

def mode_data(T):
    cols=tuple(unfolding_columns(T,DIMS,i) for i in range(3))
    data=tuple(exact_rank_and_families(cols[i],DIMS[i]) for i in range(3))
    return cols,data

def supp(mask,dim): return frozenset(i for i in range(dim) if (mask>>i)&1)

def maximal_sound_union(T,ams,bms,cms):
    A=tuple(supp(x,2) for x in ams); B=tuple(supp(x,4) for x in bms); C=tuple(supp(x,4) for x in cms)
    covered=set()
    for aa,bb,cc in product(A,B,C):
        box=frozenset(product(aa,bb,cc))
        if box and box<=T: covered.update(box)
    return frozenset(covered)

def main():
    bad=tensor_from_word(BAD_WORD,DIMS)
    require(len(bad)==22,'bad positive count')
    cols,data=mode_data(bad)
    require(tuple(r for r,_ in data)==(2,3,3),'bad mode ranks')
    expA=frozenset(((0x01,0x02),))
    expB=frozenset(((0x03,0x06,0x09),))
    expC=frozenset(((0x03,0x09,0x0E),))
    require(data[0][1]==expA,'unique A basis')
    require(data[1][1]==expB,'unique B basis')
    require(data[2][1]==expC,'unique C basis')
    target=(0,1,1); require(target in bad,'target positive')
    blockers={(0x03,0x03):(0,0,0),(0x03,0x0E):(0,1,2),(0x06,0x03):(0,2,1),(0x06,0x0E):(0,2,2)}
    seen=set(); bbase=next(iter(expB)); cbase=next(iter(expC))
    for bm,cm in product(bbase,cbase):
        if ((bm>>1)&1) and ((cm>>1)&1):
            seen.add((bm,cm)); z=blockers[(bm,cm)]
            require(z not in bad,f'blocking zero {bm:x},{cm:x}')
            require((bm>>z[1])&1 and (cm>>z[2])&1,'blocker lies in box')
    require(seen==set(blockers),'four candidate lifts')
    literal2=(1,2); literal4=(1,2,4,8)
    require(maximal_sound_union(bad,literal2,bbase,literal4)==bad,'profile (2,3,4)')
    require(maximal_sound_union(bad,literal2,literal4,cbase)==bad,'profile (2,4,3)')

    good=tensor_from_word(GOOD_WORD,DIMS)
    _,gdata=mode_data(good)
    require(tuple(r for r,_ in gdata)==(2,3,3),'good mode ranks')
    phi=(0,1,2,2)
    core=frozenset((a,b,c) for a,b,c in bad if b<3 and c<3)
    rebuilt=frozenset((a,b,c) for a in range(2) for b in range(4) for c in range(4) if (a,phi[b],phi[c]) in core)
    require(rebuilt==good,'good exact (2,3,3) Tucker decomposition')
    print(f'PASS boolean-tucker-junction checks={CHECKS} bad={BAD_WORD:#x} good={GOOD_WORD:#x}')

if __name__=='__main__': main()
