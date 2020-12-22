#!/usr/bin/python3

freq = {'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253, 'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094, 'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025, 'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929, 'q': .00095, 'r': .05987, 's': .06327, 't': .09056, 'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150, 'y': .01974, 'z': .00074, ' ': .13000}
get_english_score = lambda input_bytes: sum([freq.get(chr(byte), 0) for byte in input_bytes.lower()])
xor = lambda msg, key: b''.join([bytes([byte ^ key[i%len(key)]]) for i,byte in enumerate(msg)])

def solve_xor(cip: bytes) -> bytes:
	scr = [get_english_score(xor(cip, bytes([i]))) for i in range(255)]
	return bytes([scr.index(max(scr))])

if __name__ == '__main__':
	cip = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
	assert xor(cip,solve_xor(cip)) == b"Cooking MC's like a pound of bacon"