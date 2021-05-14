# Diffie-Hellman Key Exchange
Absolute security of communication is possible only if the key for an encryption system is only known by the participants of that conversation. So the question arises how do Alice and Bob share a secret through an untrusted channel? This is where we can use a method known as the Diffie-Hellman Key Exchange. The method was first proposed by Ralph Merkle, Whitfield Diffie & Martin Hellman during the late 1970s. 

## Key Exchange

1. A generator $g$ which is public knowledge is selected by both Alice and Bob.
2. Based on the order of $g$ Alice and Bob calculates private keys $ka$ & $kb$ and public keys $pb_a = g^{ka}$ & $pb_b = g^{kb}$ are generated respectively.
3. Alice and Bob exchanges public keys & calculates the shared secret by $sk = pb_a^{kb}$ and $sk = pb_b^{ka}$

The method makes use of the irreversible property of trap functions. Trap functions are those functions that can be calculated easily using 2 or more values but it is impossible to guess the original values with just the knowledge of outcome (in this case exponentiation). It is easy to calculate $a^b$ but difficult to guess the value of b (difficulty increases as number of bits of b increase).

