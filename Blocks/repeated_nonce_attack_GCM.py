#!/usr/bin/python3

# attack on http://aes.cryptohack.org/forbidden_fruit/
import requests
import json
from Crypto.Util.number import bytes_to_long
from Crypto.Cipher import AES

loc = "http://aes.cryptohack.org/forbidden_fruit/"
s = requests.session()

IV = b"a"*12
KEY = b"a"*16

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

def encrypt(plaintext):
	header = b"CryptoHack"

	cipher = AES.new(KEY, AES.MODE_GCM, nonce=IV)
	encrypted = cipher.update(header)
	ciphertext, tag = cipher.encrypt_and_digest(plaintext)

	return {
		"nonce": IV.hex(),
		"ciphertext": ciphertext.hex(),
		"tag": tag.hex(),
		"associated_data": header.hex(),
	}

# def encrypt(inp: bytes) -> dict:
# 	inp = loc + f"encrypt/{hex(bytes_to_long(inp))[2:]}"
# 	print(inp)
# 	return json.loads(s.get(inp).text)

splt = lambda txt: [txt[i:i+16] for i in range(0, len(txt), 16)]
def get_cofs(data: dict) -> dict:
	co = []
	ct = len(data["ciphertext"])
	ad = len(data["associated_data"])
	co += [bytes_to_long(i) for i in splt(pad(bytes.fromhex(data["associated_data"])))]
	co += [bytes_to_long(i) for i in splt(pad(bytes.fromhex(data["ciphertext"])))]
	co += [(((8 * ad) << 64) | (8 * ct))]
	co += [bytes_to_long(bytes.fromhex(data["tag"]))]
	return co

def fn(h: int, coa: list, cob: list) -> None:
	sol = GF(0)
	coa += [0]*(len(cob)-len(coa))
	cob += [0]*(len(coa)-len(cob))
	for i,j in zip(coa, cob):
		sol = sol + i
		sol = sol + j
		sol = sol * h
		print(sol.num)

coa = get_cofs(encrypt(b"a"))
cob = get_cofs(encrypt(b"b"))
ecb = AES.new(KEY, AES.MODE_ECB)
h = bytes_to_long(ecb.encrypt(b'\x00' * 16))
fn(h, coa, cob)