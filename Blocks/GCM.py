#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util.number import long_to_bytes, bytes_to_long
from os import urandom
from random import randrange

class GF:
	def __init__(self, num):
		self.num = num

	def mul(self, x, y):
		assert x < (1 << 128)
		assert y < (1 << 128)
		res = 0
		for i in range(127, -1, -1):
			res ^= x * ((y >> i) & 1)
			x = (x >> 1) ^ ((x & 1) * 0xE1000000000000000000000000000000)
		assert res < 1 << 128
		return res

	def __add__(self, other):
		return GF(self.num^other)

	def __mul__(self, other):
		p = 0
		for i in range(16):
			p ^= self.mul(other, (self.num & 0xff) << (8 * i))
			self.num >>=8
		return GF(p)

def pad(data, sz=16, st=True):
	if len(data)%sz == 0 and st:
		return data
	else:
		return data + b"\x00"*(sz-(len(data)%sz))


class GCM:
	def __init__(self, key, nonce, auth_data=b""):
		self.key = key
		self.nonce = nonce
		self.auth_data = auth_data
		
	def ghash(self, ciphertext):
		len_ad, len_ct = len(self.auth_data), len(ciphertext)
		data = pad(self.auth_data)+pad(ciphertext)

		ecb = AES.new(self.key, AES.MODE_ECB)
		h = bytes_to_long(ecb.encrypt(b'\x00' * 16))

		tag = GF(0)
		assert len(data)%16 == 0
		for i in range(len(data) // 16):
			tag = tag + bytes_to_long(data[i * 16: (i + 1) * 16])
			tag = tag * h

		tag = tag + (((8 * len_ad) << 64) | (8 * len_ct))
		tag = tag * h
		nonce = long_to_bytes((bytes_to_long(self.nonce) << 32) | 1)
		s = bytes_to_long(ecb.encrypt(nonce))
		return (tag + s).num

	def encrypt(self, plaintext):
		counter = Counter.new(nbits=32, prefix=self.nonce, initial_value=2, allow_wraparound=False)
		aes_ctr = AES.new(self.key, AES.MODE_CTR, counter=counter)
		ct = aes_ctr.encrypt(plaintext)
		tag = self.ghash(ct)
		return ct, tag

	def decrypt(self, ct, tag):
		counter = Counter.new(nbits=32, prefix=self.nonce, initial_value=2, allow_wraparound=False)
		aes_ctr = AES.new(self.key, AES.MODE_CTR, counter=counter)
		pt = aes_ctr.decrypt(ct)
		if tag == self.ghash(ct):
			return pt
		return b""


if __name__ == '__main__':
	key = urandom(16)
	plaintext = urandom(randrange(1<<4, 1<<6))
	auth_data = urandom(randrange(1<<4, 1<<5))
	init_value = urandom(12)

	ot_gcm = AES.new(key, AES.MODE_GCM, nonce=init_value)
	enc = ot_gcm.update(auth_data)
	sol = ot_gcm.encrypt_and_digest(plaintext)

	enc = GCM(key, init_value, auth_data)
	ct, tag = enc.encrypt(plaintext)
	assert sol[0]==ct and bytes_to_long(sol[1])==tag
	print("Ciphertext:\t", hex(bytes_to_long(ct)))
	print("Tag:\t\t",hex(tag))

	pt = enc.decrypt(ct, tag)
	print("plaintext:\t", hex(bytes_to_long(pt)))

	ot_gcm = AES.new(key, AES.MODE_GCM, nonce=init_value)
	enc = ot_gcm.update(auth_data)
	sol = ot_gcm.decrypt_and_verify(sol[0], sol[1])
	assert sol == pt and pt == plaintext