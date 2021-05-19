#!/usr/bin/python3
from Crypto.Util.number import *

def genKey(size):
	p = getPrime(size)
	q = getPrime(size)
	e = 0x10001
	N = p*q
	d = inverse(e,(p-1)*(q-1))
	return {'e':e,'N':N},{'d':d,'N':N}

def blind(M, r, pub):
	return pow(M*(r**pub['e']),1,pub['N'])

def sign(M, prv):
	return pow(M,prv['d'],prv['N'])

def unblind(S, r, pub):
	return pow(S*inverse(r,pub['N']),pub['e'],pub['N'])

def main():
	msg = b"This is a dangerous message!!"
	pub, prv = genKey(1024)
	M = blind(bytes_to_long(msg),2,pub)
	S = sign(M,prv)
	print(long_to_bytes(unblind(S,2,pub)))

if __name__ == '__main__':
	main()