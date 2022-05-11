import base64
import os
import sys
from mod import gen

cipher=(gen.create_cipher(sys.argv[1]))
text=gen.decrypt_cipher(cipher)
print(text)


