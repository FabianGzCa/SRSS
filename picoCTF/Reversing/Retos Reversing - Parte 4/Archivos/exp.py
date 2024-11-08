cifrado = open("rev_this", "r").read()

print(cifrado)

flag = ""

for i in range(8, len(cifrado)-1):
	if (i & 1 == 0):
		flag += chr( ord(cifrado[i])-5 )
	else:
		flag += chr( ord(cifrado[i])+2 )

print (flag)
