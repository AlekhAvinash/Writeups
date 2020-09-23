#!/usr/bin/python3
from Crypto.Util.number import inverse

class ecurve:
	def __init__(self, a, b, pr=None):
		self.a = a
		self.b = b
		self.pr = pr
		self.discriminant = lambda a, b: -16*(4*a**3 + 27*b**2)
		self.testCurve()

	def testCurve(self):
		try:
			val = self.discriminant(self.a,self.b)
			if(self.pr):
				assert val%self.pr != 0
			else:
				assert val != 0
		except:
			raise Exception("Invalid input for a, b.")

	def new_pt(self, x=None, y=None):
		return point(self.a, self.b, self.pr, x, y)

	def __str__(self):
		return 'y^2 = x^3 + %Gx + %G' % (self.a, self.b)
		
class point(ecurve):
	def __init__(self, a, b, pr, x, y):
		super(point,self).__init__(a, b, pr)
		self.x = x
		self.y = y
		self.val = lambda x,y:(x**3 + self.a*x + self.b) - (y**2)
		if(x or y):
			point.testPoint(self)

	def testPoint(self):
		try:
			if(self.pr):
				assert self.val(self.x,self.y)%self.pr == 0
			else:
				assert round(self.val(self.x,self.y)) == 0
		except:
			raise Exception("Invalid input for x, y.")
	
	def __add__(self, other):
		o = ecurve.new_pt(self)
		if(o == self):
			return other
		elif(o == other):
			return self
		elif self==other:
			if(self.pr):				
				if (self.y+other.y)%self.pr==0:
					return o
				lmd = ((3*self.x**2+self.a)*inverse(2*self.y,self.pr))%self.pr
			else:
				if (self.y+other.y)==0:
					return o
				lmd = (3*self.x**2+self.a)/(2*self.y)
		else:
			if(self.pr):
				lmd = ((other.y-self.y)*inverse(other.x-self.x,self.pr))%self.pr
			else:
				lmd = (other.y-self.y)/(other.x-self.x)
		x3 = ((lmd**2)-self.x-other.x)
		if(self.pr):
			x3 = x3%self.pr
			return ecurve.new_pt(self,x3,(lmd*(self.x-x3)-self.y)%self.pr)
		else:
			return ecurve.new_pt(self,x3,lmd*(self.x-x3)-self.y)

	def __mul__(self,n):
		R = ecurve.new_pt(self)
		while(n!=0):
			if n%2 == 1:
				R = self+R
			n//=2
			self +=self
		return R

	def __rmul__(self,n):
		return self.__mul__(n)

	def __eq__(self, other):	
		return (self.x,self.y)==(other.x,other.y)

	def __ne__(self, other):
		return (self.x,self.y)==(other.x,-other.y)

def main():
	e = ecurve(497,1768)
	p = e.new_pt(28,194)
	v = 3*p
	print(v.x,v.y)
		
if __name__ == '__main__':
	main()