#!/usr/bin/python3

def xor(pt, key):
	return b"".join([bytes([key^i]) for i in pt])

def main():
	pt = input("Enter string: ").encode('utf-8')
	key = input("Enter key: ")

	assert len(key)==1
	print("Xor ed string: ",xor(pt,ord(key)))

if __name__ == '__main__':
	main()