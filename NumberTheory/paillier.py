#!/usr/bin/python3
from Crypto.Util.number import getPrime, GCD, inverse
from random import randint

class publickey():
	def __init__(self, n):
		self.n = n
		self.n_sq = n*n
		self.g = n+1

class privatekey(object):
	def __init__(self, p, q):
		self.l = (p-1)*(q-1)
		self.n = p*q
		self.m = inverse(self.l,self.n)
		self.L = lambda x: (x-1)//self.n						

def keygen(sz):
	phi = lambda p,q:(p-1)*(q-1)
	while(True):
		p, q = (getPrime(sz) for i in range(2))
		if GCD(p*q,phi(p,q))==1:
			break
	return publickey(p*q), privatekey(p,q)

encrypt = lambda pb, m: pow(pb.g, m, pb.n_sq)*pow(randint(1,pb.n-1), pb.n, pb.n_sq)%pb.n_sq
decrypt = lambda pb, pv, c: (pv.L(pow(c, pv.l, pb.n_sq))*pv.m)%pb.n
add_ciphers = lambda pb, a, b: (a*b)%pb.n_sq
add_const = lambda pb, c, const: add_ciphers(pb, pow(pb.g, const, pb.n_sq),c)
mul_const = lambda pb, c, const: pow(c, const, pb.n_sq)

def main():
	pb, pv = keygen(1024)
	eg_a = encrypt(pb, 12)
	print("Normal decryption: \t",decrypt(pb, pv, eg_a))
	print("Add a var to msg: \t",decrypt(pb, pv, add_const(pb, eg_a, 3)))
	print("Mul a var to msg: \t",decrypt(pb, pv, mul_const(pb, eg_a, 3)))

if __name__ == '__main__':
	main()