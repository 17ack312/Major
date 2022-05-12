from mod.crypto import encrypt,decrypt
#from crypto import encrypt,decrypt

def get_cipher(text):
    #print(text)
    temp=[];key=[]
    for t in text:
        x=ord(t)+len(text)
        key.append(len(str(x)))
        temp.append(x)
        #print(x)
    temp=("".join(map(str,temp)))
    key=str("".join(map(str,key)))
    #print(temp)
    cipher=(encrypt.hex_encrypt(temp))
    #print(cipher)
    temp=[]
    for c in cipher:
        temp.append(chr(int(c)*len(key)))
    cipher=("".join(map(str,temp)))

    return cipher,key



def get_original(cipher,key):
    text=cipher
    #print(text)
    temp=[]
    for t in text:
        temp.append(int(ord(t)/len(key)))
    temp=("".join(map(str, temp)))
    #print(temp)
    temp=(decrypt.hex_decypt(temp))
    #print(temp)
    start=0
    #print(key)
    original=[]
    for k in key:
        original.append(chr(int(temp[0:int(k)])-len(key)))
        temp=temp.removeprefix(temp[0:int(k)])
    original=str("".join(map(str,original)))
    #print(original)

    return original







#cipher,key=get_cipher("Sanjay Pal\nMOB:9876543210")
#original=get_original(cipher,key)
