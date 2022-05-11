import base64

from mod import gen

cipher=(gen.create_cipher("hello"))
text=gen.decrypt_cipher(cipher)
print(text)


