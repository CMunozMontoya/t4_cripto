import os
import time
import hashlib
import uuid

os.system('cmd /c "hashcat -m0 -a0 -o crack1.txt --outfile-format=2 archivo_1 diccionario_1.dict diccionario_2.dict --show"') #archivo 1
os.system('cmd /c "hashcat -m10 -a0 -o crack2.txt --outfile-format=2 archivo_2 diccionario_1.dict diccionario_2.dict --show"') #archivo 2
os.system('cmd /c "hashcat -m10 -a0 -o crack3.txt --outfile-format=2 archivo_3 diccionario_1.dict diccionario_2.dict --show"') #archivo 3
os.system('cmd /c "hashcat -m1000 -a0 -o crack4.txt --outfile-format=2 archivo_4 diccionario_1.dict diccionario_2.dict --show"') #archivo 4
os.system('cmd /c "hashcat -m1700 -a0 -o crack5.txt --outfile-format=2 archivo_5 diccionario_1.dict diccionario_2.dict --show"') #archivo 5

for i in range(1,5):
	#se usa sha256 + salt
	file_name = "crack" + str(i) + ".txt"
	out_name = "encoded" + str(i) + ".txt"

	in_file = open(file_name,"r")
	out_file = open(out_name,"w+")

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

	print("fin archivo ", i, "\n")