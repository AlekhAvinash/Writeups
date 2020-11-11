#!/usr/bin/python3
from gmpy2 import next_prime
class ACORN():
	def __init__(self, seed, s=2, k=150):
		self.k = k
		self.Y = next_prime(seed)
		self.M = 2**(60*s)
		self.set = {}
		self.n = 0
		self.set[self.n] = [self.Y**i for i in range(1,self.k+1)]

	def rand_int(self):
		self.n+=1
		self.set[self.n] = [self.set[self.n-1][0]]
		for i in range(1,self.k):
			self.set[self.n].append((self.set[self.n][i-1]+self.set[self.n-1][i])%self.M)
		self.set.pop(self.n-1)
		return self.set[self.n][-1]/self.M

def main():
	clss = ACORN(12345)
	for i in range(100):
		print(clss.rand_int())

if __name__ == '__main__':
	main()