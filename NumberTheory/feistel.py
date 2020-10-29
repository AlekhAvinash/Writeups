#!/usr/bin/python3
import os
class feistel():
	def __init__(self, block, fn):
		self.block = block
		self.l, self.r = self.spliter()
		self.xor = lambda a,b: b"".join([bytes([i^j]) for i,j in zip(a,b)])
		self.fn = fn

	def spliter(self):
		_len = len(self.block)//2
		return self.block[:_len],self.block[_len:]

	def round(self):
		tmp = self.r
		self.r = self.xor(self.fn(self.r, self.keygen()),self.l)
		self.l = tmp

	def keygen(self):
		return os.urandom(len(self.r))

	def nroundcip(self, n):
		for i in range(n):
			self.round()
		return self.r+self.l

def main():
	fn = lambda a,b: b"".join([bytes([i^j]) for i,j in zip(a,b)])
	cip = feistel(b'\x01\x03\x02\x04',fn)
	print(cip.nroundcip(8))

if __name__ == '__main__':
	main()