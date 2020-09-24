#!/usr/bin/python3
#demo of the diffie hellman algorithm

from Crypto.Util.number import *

class DH(object):
	def __init__(self, size):
		self.size = size
		self.pubKey = {'P':getPrime(size),'G':getRandomInteger(8)}
		self.Alice = self.genPrvKey(size)
		self.Bob = self.genPrvKey(size)
		print("[Alice] \t%d\n[Bob] \t\t%d"%(self.Alice['pub'],self.Bob['pub']))

	def genPrvKey(self, size):
		a = getRandomInteger(8)%self.pubKey['P']
		return {'pub':pow(self.pubKey['G'],a,self.pubKey['P']),'prv':a}

	def genComKey(self, pr=False):
		if(pr):
			key, base = self.Alice['prv'], self.Bob['pub']
		else:
			key, base = self.Bob['prv'], self.Alice['pub']
		return pow(base,key,self.pubKey['P'])


def main():
	d = DH(128)
	while(True):
		name = input("[Who are you?] ").lower()
		if(name == "alice"):
			print("[Alice Key]\t",d.genComKey(True))
		elif(name == "bob"):
			print("[Bob Key]\t",d.genComKey())
		elif(name == "not here!"):
			print("[Bye!!]")
			break
		else:
			raise Exception("Enter valid name.. !P")

if __name__ == '__main__':
	main()