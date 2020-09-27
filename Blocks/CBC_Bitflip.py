#!/usr/bin/python3
# demo of bitflip algo

from Crypto.Cipher import AES
from binascii import unhexlify, hexlify
from Crypto.Util.Padding import pad, unpad

KEY = b'a'*16
IV = b'a'*16
bit_flex=lambda ct, pt, idx, trgt: ct[:idx-16] + b"".join([bytes([ct[idx+i-16]^pt[idx+i]^trgt[i]]) for i in range(len(trgt))]) + ct[idx+len(trgt)-16:]

def cbc_encrypt(pt):
	cipher = AES.new(KEY, AES.MODE_CBC, IV)
	return hexlify(cipher.encrypt(pad(pt,16)))

def cbc_decrypt(ct):
	cipher = AES.new(KEY, AES.MODE_CBC,IV)
	return unpad(cipher.decrypt(unhexlify(ct)),16)


# ciphertext and part of plaintext shud be known
def bit_flip(ct, pt, idx, trgt):
	attack_byte = b''
	for i in range(len(trgt)):
		attack_byte += bytes([ct[idx+i-16]^pt[idx+i]^trgt[i]])
	return ct[:idx-16] + attack_byte + ct[idx+len(trgt)-16:]
	

def bitflip(ct, pt, idx, trgt):
	pos = idx%16
	atk_block = (idx - pos)//16
	ct = [[ct[j] for j in range(i,i+16)] for i in range(0,len(ct),16)]
	pt = [[pt[j] for j in range(i,i+16)] for i in range(0,len(pt),16)]
	for i in range(len(trgt)):
		ct[atk_block-1][pos] = ct[atk_block-1][pos]^pt[atk_block][pos]^trgt[i]
		if(pos+1==16):
			atk_block += 1
		pos = (pos+1)%16
	return b"".join([bytes([j]) for i in ct for j in i])

def main():
	print('')
	pt = b'a'*32+b'AlekhAvinash'+b'a'*16
	ct = cbc_encrypt(pt)
	print("[Original Ciphertext]\n>",ct,"\n")
	
	pt = cbc_decrypt(ct)
	print("[Original Plaintext]\n>",pt,"\n")

	idx = pt.find(b'A')-2
	trgt = b';admin=True;'
	at = hexlify(bit_flip(unhexlify(ct), pt, idx, trgt))
	print("[Attack Ciphertext]\n>",at,"\n")

	vt = hexlify(bitflip(unhexlify(ct), pad(pt,16), idx, trgt))
	print("[Attack Ciphertext]\n>",vt,"\n")

	print("[Attack Plaintext]\n>",cbc_decrypt(vt),"\n")	

	pt = cbc_decrypt(at)
	print("[Attack Plaintext]\n>",pt,"\n")

	idx = pt.find(b'dmin')-2
	trgt = b';a'
	at = hexlify(bit_flip(unhexlify(at), pt, idx, trgt))
	print("[Attack Ciphertext Pass 2]\n>",at,"\n")
	
	vt = hexlify(bitflip(unhexlify(vt), pad(pt,16), idx, trgt))
	print("[Attack Ciphertext Pass2]\n>",vt,"\n")

	print("[Attack Plaintext Pass2]\n>",cbc_decrypt(vt),"\n")	

	pt = cbc_decrypt(at)
	print("[Attack Plaintext Pass 2]\n>",pt,"\n")


if __name__ == '__main__':
	main()