class colors():
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return f"({self.a},{self.b})"

	def red(self):
		a, b = self.a, self.b
		self.a = (a+(18*b))%324
		self.b = ((18*a)-b)%324

	def green(self):
		a, b = self.a, self.b
		self.a = ((17*a)+(6*b))%324
		self.b = ((-6*a)+(17*b))%324

	def blue(self):
		a, b = self.a, self.b
		self.a = ((-10*a)-(15*b))%324
		self.b = ((15*a)-(10*b))%324


def main():
	# 1
	inst = colors(20,20)
	cols = []
	for i in range(100):
		inst.red()
		if(str(inst) not in cols):
			cols.append(str(inst))
		else:
			print(cols[-1])
			break
	print(len(cols))

	# 2
	inst = colors(20,20)
	cols = []
	for i in range(100):
		inst.blue()
		if(str(inst) not in cols):
			cols.append(str(inst))
		else:
			print(cols[-1])
			break
	print(len(cols))

	# 3
	inst = colors(20,20)
	cols = []
	for i in range(100):
		inst.green()
		if(str(inst) not in cols):
			cols.append(str(inst))
		else:
			print(cols[-1])
			break
	print(len(cols))

	# 4
	inst = colors(20,20)
	cols = []
	for i in range(100):
		inst.red()
		inst.green()
		if(str(inst) not in cols):
			cols.append(str(inst))
		else:
			print(cols[-1])
			break
	print(len(cols))

	# 5
	inst = colors(20,20)
	cols = []
	for i in range(100):
		inst.red()
		inst.blue()
		if(str(inst) not in cols):
			cols.append(str(inst))
		else:
			print(cols[-1])
			break
	print(len(cols))

	# 6
	inst = colors(20,20)
	cols = []
	for i in range(100):
		inst.green()
		inst.blue()
		if(str(inst) not in cols):
			cols.append(str(inst))
		else:
			print(cols[-1])
			break
	print(len(cols))

	# 5
	inst = colors(20,20)
	cols = []
	for i in range(100):
		inst.red()
		inst.green()
		inst.blue()
		if(str(inst) not in cols):
			cols.append(str(inst))
		else:
			print(cols[-1])
			break
	print(len(cols))

if __name__ == '__main__':
	main()
