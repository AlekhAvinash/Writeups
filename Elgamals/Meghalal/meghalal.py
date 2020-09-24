#!/usr/bin/python3
from Crypto.Util.number import *

flag = 'Some_leet_string_like_this!'
p=getPrime(1024)
g=getRandomInteger(8)
x=getRandomInteger(1024)
h=pow(g,x,p)

def enc(m):
    M = bytes_to_long(m.encode('utf-8'))
    assert len(bin(M)) < len(bin(p)), 'm too long'
    y = getRandomInteger(1024)%p
    c1 = pow(g, y, p)
    c2 = (M * pow(h, y, p) ) % p 
    return c1, c2

def dec(c1, c2):
    M = (c2 * inverse(pow(c1, x, p), p)) % p
    return str(long_to_bytes(M))[2:-1]

def login():
    c = input('Please input your access token: ').split('_')
    c1 = int(c[0], 16)
    c2 = int(c[1], 16)
    print(dec(c1,c2))
    user, role = dec(c1, c2).split('#')
    print('\nWelcome {}!'.format(user))
    print('Your role is \'{}\'.\n'.format(role))
    if role == 'overlord':
        print('Here\'s your flag: {}'.format(flag))
    print('That\'s all, nothing else happening here.')

def register():
    username = input('Your username: ')
    role = input('Your role: ')
    if role == 'overlord':
        print('nope, you\'re not the overlord...')
        return
    c = enc('%s#%s' % (username, role))
    token = '{:x}_{:x}'.format(c[0], c[1])
    print('Here is your access token:\n{}'.format(token))

if __name__ == '__main__':
    print('What do you want to do?')
    print('[1] Login')
    print('[2] Register')
    choice = input('> ')
    try:
        if choice == '1':
            login()
        elif choice == '2':
            register()
    except:
        print('something went wrong...')