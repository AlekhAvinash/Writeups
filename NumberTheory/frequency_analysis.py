#!/usr/bin/python3

freq = {'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253, 'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094, 'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025, 'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929, 'q': .00095, 'r': .05987, 's': .06327, 't': .09056, 'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150, 'y': .01974, 'z': .00074, ' ': .13000}
shift = lambda m,key : ''.join([chr(((ord(char) - 65 + key) % 26) + 65) if char.isupper() else chr(((ord(char) - 97 + key) % 26) + 97) if char.islower() else char for char in m])
def get_english_score(input_bytes, freq_dict = freq):
	return sum([freq_dict.get(chr(byte), 0) for byte in input_bytes.lower()])

def frequency_analysis(input_bytes):
	char_dict = {}
	for i in input_bytes.lower():
		if bytes([i]) not in char_dict:
			char_dict[bytes([i])] = 1
		else:
			char_dict[bytes([i])] += 1
	return char_dict

def print_dict(char_dict):
	for i,j in sorted(char_dict.items(), key=lambda a:a[1], reverse=True):
		print(i,j)

def main():
	with open('sample.txt', 'r') as f:
		pt = f.read().encode('utf-8')
	print("\n\nbefore_shift_cipher: ")
	print(pt,"\nEnglish Score of input is: ",get_english_score(pt),'\n')
	print_dict(frequency_analysis(pt))


	pt = shift(pt.decode('utf-8'),3).encode('utf-8')
	print("\n\nafter_shift_cipher: ")
	print(pt,"\nEnglish Score of input is: ",get_english_score(pt),'\n')
	print_dict(frequency_analysis(pt))

	# note frequency is identical in both cases even if text unreadable

if __name__ == '__main__':
	main()
