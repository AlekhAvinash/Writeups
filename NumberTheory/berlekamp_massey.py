#!/usr/bin/python3
from lfsr import LFSR

def Berlekamp_Massey_algorithm(sequence):
	N = len(sequence)
	s = [int(i) for i in sequence]
	for k in range(N):
		if s[k] == 1:
			break
	f = set([k + 1, 0])
	l = k + 1
	g = set([0])
	a = k
	b = 0
	for n in range(k + 1, N):
		d = 0
		for ele in f:
			d ^= s[ele + n - l]
		if d == 0:
			b += 1
		else:
			if 2 * l > n:
				f ^= set([a - b + ele for ele in g])
				b += 1
			else:
				temp = f.copy()
				f = set([b - a + ele for ele in f]) ^ g
				l = n + 1 - l
				g = temp
				a = b
				b = n - l + 1
	return f, l

def main():
	inp = LFSR(12345,[1,6,8]).output(50)
	loc, len_ = Berlekamp_Massey_algorithm(inp)
	print([i+1 for i in list(loc)[:-1]], len_)

if __name__ == '__main__':
	main()