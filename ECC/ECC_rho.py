#!/usr/bin/python3

from EllipticCurves import *
from Crypto.Util.number import inverse
from random import randrange

def rho_atk(p, q, n, bits):
    evl = lambda a, b: (p*a)+(q*b)
    fj = lambda v: int(v[len(v) - bits : len(v)], 2)
    step = lambda T, P: (T[0]+P[0], (T[1]+P[1])%n, (T[2]+P[2])%n)
    while True:
        rlst = []
        for i in range(2**bits):
            a, b = randrange(0, n),randrange(0, n)
            rlst += [(evl(a, b), a, b)]
        a, b = randrange(0,n), randrange(0,n)
        T, H = (evl(a, b),a, b) ,(evl(a, b), a, b)
        while True:
            try:
                T = step(T, rlst[fj(bin(T[0].x))])

                for i in range(2):
                    H = step(H, rlst[fj(bin(H[0].x))])
            except:
                break
            if(T[0] == H[0]):
                break

        if H[2] == T[2]:
            print('Failed')
            return
        else:
            inv = inverse((H[2]-T[2])%n, n)
            inv =  inv % n
            k = ((T[1] - H[1]) * inv) % n
            if (p*k) == q:
                return k
            else:
                continue

def main():
    e = ecurve(0,13,101)
    print(e)
    g = e.gen_pt()
    print(f'g: {g}')
    n = g.order()
    k = randrange(3, n)
    print(f'k: {k}')
    p = g*k
    v = rho_atk(g, p, n, 1)
    r = g*v
    print(f'recvrd k: {k}')
    assert p == r

if __name__ == '__main__':
    main()