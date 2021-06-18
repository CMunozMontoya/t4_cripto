import os
import hashlib
import uuid

#se usa sha256 + salt
file_name = input("nombre de archivo: ")

in_file = open(file_name,"r")
out_file = open("encoded.txt","w+")

for line in in_file:
	s = line
	b = s.encode()

	#hacer hash
	hash_object = hashlib.sha512(b)
	hex_dig = hash_object.hexdigest()

	salt = uuid.uuid4().hex #salt

	out_file.write(str(hex_dig))
	out_file.write(":")
	out_file.write(salt)
	out_file.write("\n")

in_file.close()
out_file.close()