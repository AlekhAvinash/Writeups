#!/usr/bin/python3
import math
def continuedFrac(num, denum) :
	pQuo = []
	while denum != 1:
		temp = pow(num,1,denum)
		pQuo.append(num//denum)
		num = denum
		denum = temp
		if denum == 0:
			break
	return pQuo

def divergents(pQuo) :
	(p1, p2, q1, q2) = (1, 0, 0, 1)
	for q in pQuo:
		pn, qn = q * p1 + p2, q * q1 + q2
		yield (pn, qn)
		p2, q2, p1, q1 = p1, q1, pn, qn

def WienerAttack(N, e):
	C = pow(100, e, N)
	for k,d in divergents(continuedFrac(e, N)):
		if pow(C, d, N) == 100:
			return (k,d)
	return -1

def get_pq(N, e, c) :
	phi = (e*c[1]-1)//c[0]
	a = 1
	b = -(N-phi+1)
	c = N
	delta = (b**2)-(4*a*c)
	if delta > 0 :
		x1 = (-b + math.isqrt(delta))//(2*a)
		x2 = (-b - math.isqrt(delta))//(2*a)
		if x1*x2 == N:
			return (x2, x1)
	return -1