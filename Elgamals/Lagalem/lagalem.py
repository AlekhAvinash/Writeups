#!/usr/bin/python3
from Crypto.Util.number import *

FLAG = b'Some_leet_string_like_this!'

size = 2048
rand_state = getRandomInteger(size//2)

def keygen(size):
  q = getPrime(size)
  k = 2
  while True:
    p = q * k + 1
    if isPrime(p):
      break
    k += 1
  g = 2
  while True:
    if pow(g, q, p) == 1:
      break
    g += 1
  A = getRandomInteger(size) % q
  B = getRandomInteger(size) % q
  x = getRandomInteger(size) % q
  h = pow(g, x, p)
  return (g, h, A, B, p, q), (x, )

def rand(A, B, M):
  global rand_state
  rand_state, ret = (A * rand_state + B) % M, rand_state
  return ret

def encrypt(pubkey, m):
  g, h, A, B, p, q = pubkey
  assert 0 < m <= p
  r = rand(A, B, q)
  c1 = pow(g, r, p)
  c2 = (m * pow(h, r, p)) % p
  return (c1, c2)

def main():
  pubkey, privkey = keygen(size)
  m = bytes_to_long(FLAG)
  c1, c2 = encrypt(pubkey, m)
  c1_, c2_ = encrypt(pubkey, m)
  with open("enc.py","w") as f:
    f.truncate(0)
    f.write("pubkey="+str(pubkey))
    f.write("\nc1="+str(c1)+"\nc2="+str(c2))
    f.write("\nc1_="+str(c1_)+"\nc2_="+str(c2_))

if __name__ == '__main__':
  main()