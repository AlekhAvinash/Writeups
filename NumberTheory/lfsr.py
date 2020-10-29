class LFSR():
	def __init__(self, init, loc):
		self.state = init
		self.len = len(bin(init))-2
		self.loc = loc
		assert len(loc)<= self.len

	def next(self):
		ls = 0
		for i in self.loc:
			ls ^=(self.state>>i)
		ls &= 1

		ret = self.state&1
		self.state = (ls<<self.len)|(self.state>>1)
		
		return ret

def main():
	clss = LFSR(12345,[1,2,3,4])
	for i in range(10):
		print(bin(clss.state))
		print(clss.next())

if __name__ == '__main__':
	main()