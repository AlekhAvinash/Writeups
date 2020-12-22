#!/usr/bin/python3
from Crypto.Util.number import inverse, getPrime
from collections import namedtuple
from random import randint

Point = namedtuple("Point", "x y")
class ECC():
    def __init__(self, pv, P = None, G = None):
        self.pv = pv
        self.P = P or getPrime(255)
        self.G = G or self.gen_base()
        self.O = 'Origin'

    def check_point(self, P):
        if P == self.O:
            return True
        else:
            return (P.y**2 - (P.x**3 + self.pv.x*P.x + self.pv.y)) % self.p == 0\
                    and P.x in range(self.P) and P.y in range(self.P)

    def point_inverse(P):
        if P == O:
            return P
        return Point(P.x, -P.y % self.P)

    def double_and_add(self, P, n):
        Q = P
        R = self.O
        while n > 0:
            if n % 2 == 1:
                R = self.point_addition(R, Q)
            Q = self.point_addition(Q, Q)
            n = n // 2
        assert self.check_point(R)
        return R

    def point_addition(self, P, Q):
        if P == self.O:
            return Q
        elif Q == self.O:
            return P
        elif Q == self.point_inverse(P):
            return O
        else:
            if P == Q:
                lam = (3*P.x**2 + self.pv.x)*inverse(2*P.y, self.P)
            else:
                lam = (Q.y - P.y) * inverse((Q.x - P.x), self.P)
            lam %= self.P
        Rx = (lam**2 - P.x - Q.x) % self.P
        Ry = (lam*(P.x - Rx) - P.y) % self.P
        R = Point(Rx, Ry)
        assert self.check_point(R)
        return R

    def gen_base(self):
        g_x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
        g_y = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
        return Point(g_x, g_y)

def main():
    ec = ECC(Point(a,b))
    n = randint(1, p)
    public = ec.double_and_add(G, n)

if __name__ == '__main__':
    main()