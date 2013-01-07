import sys, hashlib
password = str(sys.argv[1])
preiterations = int(sys.argv[2])

pad = hashlib.sha512(password)


for i in range(preiterations):
	newpad = hashlib.sha512(pad.digest())
	pad = newpad
	
char = 0
plaintext=open(sys.argv[3],'r')
cyphertext=open(sys.argv[3]+".enc",'wb')
for read in plaintext.readlines():
	curtext = ""
	for c in read:
		if char >= 63:
			pad.update(pad.digest())
			char = 0
		cyphertext.write(chr(ord(c) ^ ord(pad.digest()[char])))
		char += 1
