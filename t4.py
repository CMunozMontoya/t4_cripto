import os
import time
import hashlib
import uuid

p = True #pasas

os.system("hashcat -m0 -a0 -o crack1.txt Hashes/archivo_1 diccionarios/diccionario_1.dict diccionarios/diccionario_2.dict --potfile-disable") #archivo 1
if p:
	os.system("pause")

os.system("hashcat -m10 -a0 -o crack2.txt Hashes/archivo_2 diccionarios/diccionario_1.dict diccionarios/diccionario_2.dict --potfile-disable") #archivo 2
if p:
	os.system("pause")

os.system("hashcat -m10 -a0 -o crack3.txt Hashes/archivo_3 diccionarios/diccionario_1.dict diccionarios/diccionario_2.dict --potfile-disable") #archivo 3
if p:
	os.system("pause")

os.system("hashcat -m1000 -a0 -o crack4.txt Hashes/archivo_4 diccionarios/diccionario_1.dict diccionarios/diccionario_2.dict --potfile-disable") #archivo 4
if p:
	os.system("pause")

os.system("hashcat -m1800 -a0 -o crack5.txt Hashes/archivo_5 diccionarios/diccionario_1.dict diccionarios/diccionario_2.dict --potfile-disable") #archivo 5
if p:
	os.system("pause")

#las pausas son para sacar pantallazos

