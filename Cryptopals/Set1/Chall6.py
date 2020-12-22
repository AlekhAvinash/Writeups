#!/usr/bin/python3
from base64 import b64decode
from Crypto.Util.number import bytes_to_long 
from Chall3 import xor, solve_xor

# Step 1
KEYSIZE = range(2, 41)

# Step 2
hamming_dist = lambda x, y: sum([int(i) for i in bin(bytes_to_long(xor(x,y)))[2:]])
assert hamming_dist(b"this is a test", b"wokka wokka!!!") == 37

# Step 3+4
split_blocks = lambda cip, key: [cip[i:i+key] for i in range(0,len(cip),key)]
func_blocks = lambda blks, fnc: [fnc(blks[i],blks[i-1]) for i in range(1,len(blks))]
def find_key_size(cip: bytes) -> bytes:
	normalized_val_list = []
	for key_size in KEYSIZE:
		blocks = split_blocks(cip, key_size)[:-1]
		avg_ham_dist = sum(func_blocks(blocks, hamming_dist))/(len(blocks)-1)
		normalized_val_list += [avg_ham_dist/key_size]
	return normalized_val_list.index(min(normalized_val_list))+KEYSIZE[0]

# Step 5+6+7+8
byte_split_blocks = lambda blocks, key:b"".join([bytes([blk[key]]) for blk in blocks])
def find_key(cip: bytes, key_size: bytes) -> bytes:
	blocks = split_blocks(cip, key_size)[:-1]
	return b"".join([solve_xor(byte_split_blocks(blocks, i)) for i in range(key_size)])

def break_repeated_xor(cip: bytes) -> bytes:
	return find_key(cip, find_key_size(cip))

if __name__ == '__main__':
	cip = b64decode(open('6.txt','r').read())
	plt = b64decode(open('6_sol.txt', 'r').read())
	assert xor(cip, break_repeated_xor(cip)) == plt