import glob
import time
import os
import argon2
from argon2 import PasswordHasher

ph = argon2.PasswordHasher()

path = os.curdir

i = 0
file = open("argon2_files","w+")
for filename in glob.glob(os.path.join(path,'crack*')):
	start = time.time()
	file2 = open(filename, "r")
	print("Archivo ", filename)
	for line in file2:


		if( i == 0):
			line = line[33:len(line) - 1]
		elif(i == 1 or i == 2):
			line = line[50:len(line) - 1]
		elif(i == 3):
			line = line[33:len(line) - 1]
		else:
			line = line[1:len(line) - 1]
		file.write((ph.hash(line)) +'\n')
	i += 1
	end = time.time()
	print("Archivo ", filename, " finalizado en ", end-start, "[s]")
file.close()
