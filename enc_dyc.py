from mod import engine


text=input("enter msg:")
cipher,key=engine.get_cipher(text)
original=engine.get_original(cipher,key)

print("encrypted :",cipher)
print("decrypted :",original)