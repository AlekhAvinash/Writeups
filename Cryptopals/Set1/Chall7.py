#!/usr/bin/python3

from Crypto.Cipher import AES
from base64 import b64decode
KEY = b"YELLOW SUBMARINE"
cipher = AES.new(KEY, AES.MODE_ECB)

if __name__ == '__main__':
	ct = b64decode(open('7.txt','r').read())
	pt = b64decode(open('7_sol.txt','r').read())
	assert cipher.decrypt(ct) == pt