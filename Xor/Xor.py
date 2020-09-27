#!/usr/bin/python3

class key_xor_exploit():
    def __init__(self):
        self.printx = lambda key, msg: print("\nKey: {}\n\nMessage: {}\n".format(key, msg))
        self.xor = lambda msg, key: b''.join([bytes([byte ^ key[i%len(key)]]) for i,byte in enumerate(msg)])

    def single_xor(self, cp, pr=False):
        potential_messages = {}
        freq = {'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253, 'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094, 'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025, 'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929, 'q': .00095, 'r': .05987, 's': .06327, 't': .09056, 'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150, 'y': .01974, 'z': .00074, ' ': .13000}
        get_english_score = lambda input_bytes: sum([freq.get(chr(byte), 0) for byte in input_bytes.lower()])
        for key_value in range(256):
            pt = self.xor(cp, key_value.to_bytes(1,'big'))
            potential_messages[key_value] = get_english_score(pt)
        key = bytes([sorted(potential_messages.items(), key=lambda x: x[1], reverse=True)[0][0]])
        pt = self.xor(cp, key)
        if pr: self.printx(pt, key)
        return (pt, key)

    def IC_key_length(self, cp):
        from collections import Counter
        IC = lambda text:sum([j*(j-1) for i,j in Counter(text).items()])/(len(text)*len(text[:-1]))
        sizes,uplim = {},41
        if(len(cp)//2<uplim):
            uplim=len(cp)//2-2
        for size in range(2,41):
            chunks = [b"".join([bytes([cp[i*size+j]]) for i in range(len(cp)//size)]) for j in range(size)]
            sizes[size] = sum([IC(i) for i in chunks])/len(chunks)
        return sorted(key_lengths.items(), key=lambda x: x[1], reverse=True)[0][0]

    def key_length(self, cp):
        average_distances = {}
        xlen = lambda x: len(x) - len(x)%2
        ham_dist = lambda str1, str2: sum([int(bit) for b1, b2 in zip(str1, str2) for bit in bin(b1 ^ b2)[2:]])
        for keysize in range(2,41):
            chunks = [cp[i:i+keysize] for i in range(0, len(cp), keysize)]
            distances = [float(ham_dist(chunks[i],chunks[i+1]))/keysize for i in range(0,xlen(chunks),2)]
            average_distances[keysize] = sum(distances) / len(distances)
        return sorted(average_distances.items(), key=lambda x: x[1])[0][0]

    def repeating_xor(self, cp, pr=False):
        key_length, key = self.IC_key_length(cp), b''
        for i in range(key_length):
            block = b''.join(bytes([cp[j]]) for j in range(i, len(cp), key_length)) 
            key += self.single_xor(block)[1]
        pt = self.xor(cp, key)
        if pr: self.printx(pt, key)
        return (pt, key)

def main():
    from msg import msg
    enc = key_xor_exploit()
    cip = enc.xor(msg,b'heya')
    pt, key = enc.repeating_xor(cip,True)
    cip = enc.xor(msg,b'a')
    pt, key = enc.single_xor(cip,True)

if __name__ == '__main__':
    main()