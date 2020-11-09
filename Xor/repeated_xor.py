#!/usr/bin/python3

def xor(pt, key):
	return b"".join([bytes([key[i%len(key)]^j]) for i,j in enumerate(pt)])

def main():
	pt = input("Enter String: ").encode('utf-8')
	key = input("Enter String: ").encode('utf-8')
	
	print("Xor ed string: ",xor(pt,key))


if __name__ == '__main__':
	main()