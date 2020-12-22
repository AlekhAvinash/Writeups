#!/usr/bin/python3

freq = {'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253, 'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094, 'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025, 'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929, 'q': .00095, 'r': .05987, 's': .06327, 't': .09056, 'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150, 'y': .01974, 'z': .00074, ' ': .13000}
get_english_score = lambda input_bytes: sum([freq.get(chr(byte), 0) for byte in input_bytes.lower()])
xor = lambda msg, key: b''.join([bytes([byte ^ key[i%len(key)]]) for i,byte in enumerate(msg)])

def solve_xor(cip):
	scr = [get_english_score(xor(cip, bytes([i]))) for i in range(255)]
	return xor(cip,bytes([scr.index(max(scr))]))

if __name__ == '__main__':
	file_strings = open('4.txt', 'r').read().split('\n')
	xored_list = [solve_xor(bytes.fromhex(i)) for i in file_strings]
	
	scr = []
	for i in xored_list:
		try:
			scr += [get_english_score(i)]
		except:
			pass
	assert xored_list[scr.index(max(scr))] == b'Now that the party is jumping\n'