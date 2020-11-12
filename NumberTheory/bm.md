# Exploiting LFSRs
LFSR (Linear Feedback Shift Register) is a popular PRNG. Its model was used to build outer shift register random number generators. It is a rather simple method which is quite lightweight and efficient. But its benefits have a downside of being easy to predict. The Berlekamp-Massey algorithm is a method used to exploit and predict the next output of the generator.

## BM (Berlekamp-Massey) Algorithm
In an LFSR there are 2 components that help to initialize the PRNG. These are the seed and the location in which the designated operation (in most cases this is an XOR operation) is carried out. 
```py
	class LFSR():
	def __init__(self, init, loc=[1,4,9]):
		self.state = init
		self.loc = loc
```
But in LFSRs, the initial state is always reflected in the random output initially. This property of LFSRs applies to any point in the output stream. If we know the current state (block of a length of initial seed and contains previous outputs of LFSR).
```py
	clss = LFSR(12345)
	test = clss.output(20)
	print(test)			# 10011100000011010101
	print(int(test[13::-1],2))	# 12345 == input seed
```
Knowing this property one can essentially predict the next output of an LFSR if the location and length of initial input are known. These unknowns are derived using the algorithm if enough input is provided.

## Demo
Consider a situation where you are given a stream of 1000 random outputs from an LFSR generator. The seed is unknown and the positions (loc) are unknown. And you are asked to predict the next 100 outputs.
```py
	clss = LFSR(seed,loc)
	print(clss.output(1000))

	inp = input("Predict next 100 outputs: \n> ")
	if inp == clss.output(100):
		print("FLAG")
```
Here using the BM algorithm, this seed and loc variables can be recovered only using the known 1000 outputs.
```py
	ret = berlekamp_massey_algorithm(inp)

	seed = int(inp[ret[0]-1::-1],2)
	loc = [i+1 for i,j in enumerate(ret[1]) if(j)]
```
And the next 100 outputs can be calculated!

## Conclusion
Although the mathematics behind the BM algorithm is quite interesting, the scope of which is beyond our current scope of education. But one thing to note from this brief explanation is that since LFSRs follow an algorithm, they can be reverse-engineered. Thus making the random number generators not so random anymore. The BM algorithm is one among many methods proving the above-stated theory. Modern PRNGs are not so easily reversible but as time progress we get to see what types of algorithms are harder to break vise versa.

## Resources
- https://en.wikipedia.org/wiki/Berlekamp%E2%80%93Massey_algorithm

The python implementation of the demo can be found [here](https://github.com/AlekhAvinash/Writeups/blob/master/NumberTheory/lfsr.py) and the exploit [here](https://github.com/AlekhAvinash/Writeups/blob/master/NumberTheory/berlekamp_massey.py)
