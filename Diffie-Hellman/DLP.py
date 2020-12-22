#!/usr/bin/python3
from Crypto.Util.number import getPrime
def enc(m):
    x = (m.bit_length()*4)//3
    p = getPrime(x)
    return pow(2, m, p), p

def bsgs(g, a, p):
    m = round((p-1)**0.5)
    lookup_table = {pow(g, i, p): i for i in range(m)}
    c = pow(g, m*(p-2), p)
    for j in range(m):
        x = (a*pow(c, j, p)) % p
        if x in lookup_table:
            return j*m + lookup_table[x]
    return None

def main():
    m = 4484446120
    a, p = enc(m)
    x = bsgs(2, a, p)
    print(x)

if __name__ == '__main__':
    main()