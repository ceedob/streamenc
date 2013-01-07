#!/usr/bin/python
import sys, hashlib
if "-h" in sys.argv or len(sys.argv)==1:
	print """Streamenc file encryption:\nUsage: streamenc <file>"""
	exit()
password = raw_input("password:   ")
preiterations = int(raw_input("hash loops: "))

pad = hashlib.sha512(password)


for i in range(preiterations):
	newpad = hashlib.sha512(pad.digest())
	pad = newpad
	

plaintext=open(sys.argv[1],'r')
if sys.argv[1][-4:] != ".enc":
	filename = sys.argv[1]+".enc"
else:
	filename = sys.argv[1][:-4]+".plaintext"
cyphertext=open(filename,'wb')

text = plaintext.read()

def runoperation(password, loops, string):
	output = ""
	curtext = ""
	char = 0
	for c in string:
		if char >= 63:
			pad.update(pad.digest())
			char = 0
		output+=(chr(ord(c) ^ ord(pad.digest()[char])))
		char += 1
	return output

	

cyphertext.write(runoperation(password, preiterations, text))

