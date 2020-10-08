# Blinding Attack on RSA Digital Signatures

## Introduction
RSA security is often excecuted without the knowledge of the user. These automated process are relies on an application of RSA called Digital Signatures. Basically when Alice encrypts a msg with Bob's public key, only Bob can decrypt the message. This proof of identity is called Digital Signatures. Often Bob sets up defences so that he doesn't sign some dangerous messages sent by Marvin ([Someone pretending to be Alice](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)). But Blinding Attack utilises another property of RSA to bypass these defences.
<p><a href="https://commons.wikimedia.org/wiki/File:Man_in_the_middle_attack.svg#/media/File:Man_in_the_middle_attack.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Man_in_the_middle_attack.svg/1200px-Man_in_the_middle_attack.svg.png" alt="Man in the middle attack.svg"></a><br>

## Digital Signatures
Digital Signatures usually works in three steps:-
1. Alice sends a message M (M < N) to Bob.
2. Bob checks if the message falls within his defencive rules and signs the message (C = M&#x1D48; % N) and sends it back to Alice.
<p align="center">
  <img src="Img/enc.png">
</p>
3. Alice decrypts the message (M = C&#x1D49; % N) and checks if the returned message is the same as the one she sent.
<p align="center">
  <img src="Img/dec.png">
</p>

## Blinding Attack
When Marvin tries to send a message similar to Alices, Bob notices that the message has some dangerous messages in it and refuses to sign the message. But RSA doesn't have any checking mechanisms inherently, these constrains can be bypassed easily. Sometimes just multipling the dangerous message with a prime number would suffice. So Marvin can attempt a Blinding Attack by using the following steps:-
1. Preapre a buffer r&#x1D49; (r = small integer and e = public key) and send messge multiplied with buffer.
    * These buffers are often referred to as Blinding Factors
<p align="center">
  <img src="Img/blinding.png">
</p>

2. Since Bob only checks for certain strings or characters, Marvin's message will be approved because from Bob's perspective, Marvin is sending a random message that don't contain any unwanted text. And bob returns the signed message.
<p align="center">
  <img src="Img/blinding-sign.png">
</p>

3. Now all Marvin has to do is decrypt the message and remove the blinding factor.
<p align="center">
  <img src="Img/unblinding.png">
</p>

Here is a small implementation [blinding.py](https://github.com/AlekhAvinash/Writeups/blob/master/RSA/blinding.py).
## Reference: 
- https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf
- https://masterpessimistaa.wordpress.com/2017/07/10/blinding-attack-on-rsa-digital-signatures/
