#!/usr/bin/env python3
A = (
    (0,1,1,0,1),
    (1,0,1,0,1),
    (1,0,0,1,0),
    (0,1,0,1,0),
    (1,1,0,1,1),
)
ELL=(-1,1,-1,1,0)
RNULL=(-1,-1,0,1,1)
RECTS=(
((2,7,9),(10,13,20,23)),((10,14,20),(1,4,16,19)),
((5,9),(1,4,11,14,21,24)),((7,9,12,14,22),(0,3)),
((18,19),(6,8,16,18)),((13,23,24),(1,3,16,18)),
((3,23,24),(6,8,21,23)),((1,),(5,7,9,20,22,24)),
((8,),(1,3,11,13,21,23)),((2,17),(5,8)),
((0,1,5,6),(12,)),((10,11),(2,17)),
((0,),(6,7,9,11,14,21,22,24)),((5,6,20,21),(2,22)),
((16,19,21,24),(5,9,15,19)),((4,22),(5,8,20,23)),
((3,4),(11,13)),((4,20),(6,9,21,24)),
((15,),(6,7,9,16,17,19)),((11,),(0,4,15,19)),
((6,21,24),(0,4,20,24)),((16,20,21),(7,17)),
((1,4,6),(10,14)),((12,14,17,22),(15,18)),
)
def check(c,m):
    if not c: raise AssertionError(m)
def det4(M):
    M=[list(r) for r in M]; sign=1; prev=1
    for k in range(3):
        p=next(i for i in range(k,4) if M[i][k])
        if p!=k: M[k],M[p]=M[p],M[k]; sign=-sign
        q=M[k][k]
        for i in range(k+1,4):
            for j in range(k+1,4):
                M[i][j]=(M[i][j]*q-M[i][k]*M[k][j])//prev
        for i in range(k+1,4): M[i][k]=0
        prev=q
    return sign*M[3][3]
def kron(A,B):
    return tuple(tuple(A[i//5][j//5]*B[i%5][j%5] for j in range(25)) for i in range(25))
def main():
    check(all(sum(ELL[i]*A[i][j] for i in range(5))==0 for j in range(5)), 'bad left null vector')
    check(all(sum(A[i][j]*RNULL[j] for j in range(5))==0 for i in range(5)), 'bad right null vector')
    M=tuple(tuple(A[i][j] for j in (0,1,2,3)) for i in (0,1,2,4))
    check(abs(det4(M))==1, 'displayed 4x4 minor is not unimodular')
    candidates=0
    for um in range(1,32):
        u=tuple((um>>i)&1 for i in range(5))
        if not u[2] or sum(ELL[i]*u[i] for i in range(5))!=0: continue
        for vm in range(1,32):
            v=tuple((vm>>j)&1 for j in range(5))
            if not v[0] or sum(v[j]*RNULL[j] for j in range(5))!=0: continue
            if all(not(u[i] and v[j]) or A[i][j] for i in range(5) for j in range(5)):
                candidates += 1
    check(candidates==0, 'a balanced rank-one term covers the key entry')
    T=kron(A,A)
    ones={(i,j) for i in range(25) for j in range(25) if T[i][j]}
    count={e:0 for e in ones}; area=0
    check(len(RECTS)==24, 'certificate does not contain 24 rectangles')
    for q,(rows,cols) in enumerate(RECTS,1):
        check(rows and cols, f'empty rectangle {q}')
        for i in rows:
            for j in cols:
                check(T[i][j]==1, f'rectangle {q} hits zero at {(i,j)}')
                count[(i,j)] += 1; area += 1
    check(len(ones)==196, 'unexpected tensor support size')
    check(area==196, 'rectangle areas do not sum to 196')
    check(all(v==1 for v in count.values()), 'tensor support is not partitioned exactly once')
    print('PASS: rank_bin(A)=5 and A tensor A has an exact 24-biclique partition (196/196 ones).')
if __name__=='__main__': main()
