#!/bin/python3

from random import randrange
from math import gcd

def pollard_rho(n, fn):
    if n==1:
        return 1
    if n%2==0:
        return 2
    ttle = randrange(2, n-1)
    hare = ttle
    while True:
        ttle = fn(ttle)
        for i in range(2):
            hare = fn(hare)
        if gcd(abs(ttle-hare), n)>1:
            return gcd(abs(ttle-hare), n)

if __name__ == '__main__':
    print(pollard_rho(8281, lambda x: x**2))