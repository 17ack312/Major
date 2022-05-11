#55295
import random
from mod.crypto import encrypt,decrypt


def create_cipher(text):
    temp=[]
    for i in text:
        #print(i,ord(i))
        #print(chr(ord(i)+len(text)))
        temp.append(chr(ord(i)+len(text)))

    cipher=(encrypt.hex_encrypt("".join(map(str,temp))))
    return cipher


def decrypt_cipher(cipher):
    cipher=decrypt.hex_decypt(cipher)
    temp=[]
    for c in cipher:
        temp.append(chr(ord(c)-len(cipher)))
    text=("".join(map(str,temp)))
    return text



