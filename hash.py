import os
import hashlib

s = "lalalalala"
b = s.encode()

hash_object = hashlib.sha256(b)
hex_dig = hash_object.hexdigest()
print(hex_dig)