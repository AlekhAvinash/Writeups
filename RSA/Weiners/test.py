#!/usr/bin/python3
from sympy import nextprime
from random import randint
from Crypto.Util.number import *
from weiners import *

pt = bytes_to_long(b'ctf{this is a sample flag!!}')

def gen_test(sz):
	p, d = getPrime(sz), getPrime(sz//4)
	q = nextprime(randint(p, 2*p))
	N, phi = p*q, (p-1)*(q-1)
	e = inverse(d, phi)
	assert (3*d)**4 < N
	return (N,e,pow(pt, e, N))

if __name__ == "__main__":
	N,e,C = gen_test(512)
	d = WienerAttack(N, e)
	if d != -1 :
		print("d = "+str(d[1]))
		print('flag =',long_to_bytes(pow(C, d[1], N)))
	else:
		print("Failed")
	pq = get_pq(N, e, d)
	if pq!=-1:
		print('p =',pq[0])
		print('q =',pq[1])
		print(pq[1]*pq[0]==N)
	else:
		print('N not in format {p*q}')