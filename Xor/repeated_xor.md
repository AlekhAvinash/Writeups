# Repeated Xor
Xor ciphers have been an integral part of Cryptography. They are the basic building blocks for numerous complex encryption standards. Therefore understanding how a repeated xor cipher is implemented is crucial in one's journey through cryptography.

## Key Facts to Note
- Xor function is implimented in python as follows:-
```py 
	a^b # provided a,b are either numbers or single bytes
```
- Xor b/w  same values results in 0. Also xor b/w any value and 0, will return the same value:-
```py
	a^a==0 # fun fact:
	a^0==a # in mathematics 0 is known as the identity element of xor opt. 
```

## Implementation of Repeated Xor

Usually, the 'a' represents the plaintext and 'b' represents the key. So a plaintext 'pt' is usually XORed with a key 'key'. We can also retrieve the plaintext by XORing the result with the key.
```py
	ct = pt^key # ciphertext aka 'ct'
	pt = ct^key # since pt^key^key == pt^0 == pt
```
Now a problem arises. In most cases, we have to encrypt a long plaintext using a small key. A solution is that we can repeat the key multiple times to xor every element of the plaintext.
```py
	ct = []
	for i in pt:
		ct.append(chr(ord(i)^ord(key)))
		# ord fn converts string to ascii value and chr does vice versa.
	"".join(ct)
```
Now we encounter a weakness in our encryption system, there are only 128 characters in the ASCII table and even fewer printable characters. It would be very easy to try all possible characters until we get a match. This method is called a brute-force attack. But we can drastically improve security by increasing the length of the key string.
```py
	ct = []
	for i,j in enumerate(pt):
		# enumerate increments i value as we parse pt
		ct.append(chr(ord(key[i%len(key)])^ord(j)))
		# i%len(key) cycles through all chars in key
	"".join(ct)
```
## Conclusion
The repeated xor is in no way perfect, but this sets the baseline for many cryptographic systems. So knowledge of this simple system will set your thoughts towards the more complex methods.

[Here](https://github.com/AlekhAvinash/Writeups/blob/master/Xor/repeated_xor.py) is a link to a simple implementation of repeated xor (with a few extra changes ;).