import os
from cryptography.fernet import Fernet

s = "lalalalala"
b = s.encode()

key = Fernet.generate_key()  # store in a secure location
print("Key:", key.decode())
f = Fernet(key)
print("f: ",f)
token = f.encrypt(b)
print("token: ", token)
m = f.decrypt(token)
print(m)