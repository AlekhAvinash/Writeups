#!/usr/bin/python3

from os import urandom
from hashlib import sha256

xor = lambda x, y: b''.join([bytes([i^j]) for i, j in zip(x,y)])
hs = lambda x: sha256(x).digest()
tohex = lambda x: x.hex()
frmhex = lambda x: bytes.fromhex(x)

class merkel:
	def __init__(self, arr, ishex=False):
		arr = list(map(frmhex, arr)) if ishex else arr
		self.root = [hs(i) for i in arr]

	def make(self):
		n = len(self.root)
		while n!=1:
			if n%2!=0:
				return False
			lst = self.root[-n:]
			self.root += [hs(xor(lst[i],lst[i+1])) for i in range(0,n,2)]
			n>>=1
		return True

	def get_merkel(self):
		if self.make():
			return list(map(tohex, self.root))
		else:
			raise Exception('Wrong number of inputs..')

	def get_ver_lst(self, ele, ishex=False):
		ele = hs(frmhex(ele)) if ishex else hs(ele)
		lw, ht, idx = 0, (len(self.root)+1)>>1, self.root.index(ele)
		ret = []
		while ht!=0:
			ret += [self.root[idx+lw]]
			lw, ht, idx = lw+ht, ht>>1, idx>>1
		return list(map(tohex, ret))

	def ver_lst(self, lst, ishex=False):
		lst = list(map(frmhex, lst)) if ishex else lst
		lw, ht, idx = 0, (len(self.root)+1)>>1, self.root.index(lst[0])
		ret = True
		ctr = 0
		while ht!=0:
			ret &= lst[ctr]==self.root[idx+lw]
			ctr += 1
			lw, ht, idx = lw+ht, ht>>1, idx>>1
		return ret

def printer(lst):
	lst, ctr = lst[::-1], 1
	for i in range(1, len(lst)+1):
		print('   ->'* ctr, lst[i-1])
		if(i==((1<<ctr)-1)):
			ctr+=1

def test(n, loc):
	arr = [urandom(16) for i in range(n)]
	obj = merkel(arr[:])
	merkel_lst = obj.get_merkel()
	printer(merkel_lst)
	verify_lst = obj.get_ver_lst(arr[loc])
	print(verify_lst)
	print(obj.ver_lst(verify_lst, True))

if __name__ == '__main__':
	test(32, 3)