# Substitution Cipher (Frequency analysis)
Information can be encrypted in multiple ways, one among the most popular ways is the substitution cipher. In this method when a character is used as input, it will return some random character as output. This might seem safe but there is a huge downside. 

### Vuln
Every character in every language will have a fixed frequency (given enough information). Since the same random character will be the output for a particular character throughout the text, the number of times a particular character used is unchanged (ie the frequency is unchanged). If an attacker decides to record the frequency of each character and if he knows the language and the frequency of its characters, the attacker can simply replace the random character with the correct character and thereby revealing the secret!!

### Mitigation
When creating &/ using an encryption standard, avoid the possibility of the ciphertext resembling the original text in any sort of way. Another key point to note is that the method of encryption should use the entire text as the input to the function rather than one character at a time.

### Resources
- https://en.wikipedia.org/wiki/Frequency_analysis

Demo: [exploit.py](https://github.com/AlekhAvinash/Writeups/blob/master/NumberTheory/frequency_analysis.py)
