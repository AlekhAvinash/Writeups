#!/usr/bin/python3
class LFSR():
	def __init__(self, init, loc=[1,4,9]):
		self.state = init
		self.loc = loc
		self.len = len(bin(init))-2
		if self.len<10:
			self.state *= 100
		assert len(loc)<= self.len

	def next(self):
		ls = sum([self.state>>i for i in self.loc])%2
		ret = self.state&1
		self.state = (ls<<self.len)|(self.state>>1)
		return ret

	def output(self,n):
		return "".join([str(self.next()) for i in range(n)])

def main():
	seed = 12345
	loc = [1,2,3,6]

	clss = LFSR(seed,loc)
	print(clss.output(1000))
	
	if input("Predict next 100 outputs: \n> ") == clss.output(100):
		print("FLAG")

if __name__ == '__main__':
	main()