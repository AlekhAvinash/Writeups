# Pseudo Random Number Generator (PRNG)
Random number generators have always been topic of much debate in the scientific, mathmatics and computer science communities. Random number generators is split into 2 categories 'PRNG's (Pseudo Random Number Generators) and 'TRNG's (True Random Number Generators). Most of the debate is on which category a random number generator belongs to. 

## TRNGs Vs PRNGs
TRNG is a number generator which will always produce truly unpredictble numbers. Usually they depend on the naturally occouring randomness (lava lamps, position of atoms/stars etc). PRNG's on the other-hand depends on quite complex mathematical algorithms and usually require a secret initialiser (seed). There is alot of grey area between these categories. But computer scientists have always looked for a TRNG which depends on maths.

A good example as to why computer scientists strive for TRNGs is Security. Many Cryptographic systems rely on random number generators. If those generators were predicatable then all sense of security would be lost! But this is difficult since any mathmatical method will have some form of pattern/s.

## Popular PRNGs
The search for a perfect algorithmic random number generator started way back in the 1950s. The earliest known algorithmic PRNG is the middle-square method by J. von neumann in 1946. Since then we have come a long way towards realising our goal. And along the way we saw alot of exeptional designs. One among those which is quite popular due to its versatility and simple design is LFSRs (Linear Feedback Shift Register). This method later on gave rise to multiple impressive variations like XORshift and Mersenne Twister (one among the most common random number generators). Many other designs showed the power of simple recursive operations. One such example is the ACORN generator.

Many clever computer scientists went a completely different route. They used some of the most robust encryption algorithms to generate randomness. Some methods even relied upon the randomness of keystrokes and mouse movements. But the search for perfection is still on.

## Conclusion
Although random number generators are not perfect, they have come very close to perfection. Most of the random number generators discussed here cannot be broken without the use of high computing power. Therefore, most of today's random number generators are pretty reliable and quite hard to predict/exploit.

## Resources
- https://en.wikipedia.org/wiki/List_of_random_number_generators
- https://en.wikipedia.org/wiki/Hardware_random_number_generator
- https://en.wikipedia.org/wiki/Pseudorandom_number_generator

Implimentation of some of the more popular PRNGs
- [LSFR.py](https://github.com/AlekhAvinash/Writeups/blob/master/NumberTheory/lfsr.py)
- [ACORN.py](https://github.com/AlekhAvinash/Writeups/blob/master/NumberTheory/ACORN.py)
