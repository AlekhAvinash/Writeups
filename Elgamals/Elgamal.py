#!/usr/bin/python3
#demo of Elgamal System
from Crypto.Util.number import *

class Elgamal(object):
	def __init__(self, size, vprv=False, pubKey=None):
		self.size = size
		self.vprv = vprv
		if(pubKey):
			self.pubKey = pubKey
		else:
			self.pubKey = {'q':getPrime(size),'g':getRandomInteger(8)}
		print("[prime] %d\n[base] %d"%(self.pubKey['q'],self.pubKey['g']))
		self.Bob = self.genKey(size,True)
		self.Alice = self.genKey(size)

	def genKey(self, size, person=False):
		a = getRandomInteger(size)%self.pubKey['q']
		assert GCD(a,self.pubKey['q'])==1
		h = pow(self.pubKey['g'],a,self.pubKey['q'])
		if(person): print("[Bob] ",h)
		else: print("[Alice] ",h)
		if(self.vprv): print("[prv]",a)
		return {'pub':h,'prv':a}

	def Play(self):
		name = input("[Who is this] ").lower()
		if(name == 'alice'):
			p, h = (self.Alice['prv'], self.Bob['pub'])
		elif(name == 'bob'):
			p, h = (self.Bob['prv'], self.Alice['pub'])
		else:
			raise Exception("Enter valid name !P")
		if(self.vprv):
			p = int(input("[prv] "))
		return p, h

	def encrypt(self,msg):
		key, h = self.Play()
		s = pow(h,key,self.pubKey['q'])
		return (msg*s)%self.pubKey['q']

	def decrypt(self,cip):
		key, p = self.Play()
		s = pow(p,key,self.pubKey['q'])
		return (cip*inverse(s,self.pubKey['q']))%self.pubKey['q']

def main():
	e = Elgamal(1024)
	while(True):
		val = input("[1: Encrypt] [2: Decrypt] [3: Exit]\n[*] ")
		if(val == "1"):
			msg = bytes_to_long(input("[Msg] ").encode('utf-8'))
			cip = e.encrypt(msg)
			print("[Enc]",cip)
		elif(val == "2"):
			M = e.decrypt(int(input("[Enc] ")))
			print("[Msg]",long_to_bytes(M).decode('utf-8'),"\n\n")
		elif(val == "3"):
			print("[bye]")
			break
		else:
			raise Exception("Enter valid input !P")

if __name__ == '__main__':
	main()