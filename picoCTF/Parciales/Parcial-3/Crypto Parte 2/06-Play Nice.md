## Objetivo
Not all ancient ciphers were so bad... The flag is not in standard format. `nc mercury.picoctf.net 19354` [playfair.py](https://mercury.picoctf.net/static/9ea1604c8767cd6545948ad54670c2bf/playfair.py)

## Solución
Revisamos el código del archivo .py
```bash
❯ catn playfair.py
#!/usr/bin/python3 -u
import signal

SQUARE_SIZE = 6


def generate_square(alphabet):
	assert len(alphabet) == pow(SQUARE_SIZE, 2)
	matrix = []
	for i, letter in enumerate(alphabet):
		if i % SQUARE_SIZE == 0:
			row = []
		row.append(letter)
		if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
			matrix.append(row)
	return matrix

def get_index(letter, matrix):
	for row in range(SQUARE_SIZE):
		for col in range(SQUARE_SIZE):
			if matrix[row][col] == letter:
				return (row, col)
	print("letter not found in matrix.")
	exit()

def encrypt_pair(pair, matrix):
	p1 = get_index(pair[0], matrix)
	p2 = get_index(pair[1], matrix)

	if p1[0] == p2[0]:
		return matrix[p1[0]][(p1[1] + 1)  % SQUARE_SIZE] + matrix[p2[0]][(p2[1] + 1)  % SQUARE_SIZE]
	elif p1[1] == p2[1]:
		return matrix[(p1[0] + 1)  % SQUARE_SIZE][p1[1]] + matrix[(p2[0] + 1)  % SQUARE_SIZE][p2[1]]
	else:
		return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]

def encrypt_string(s, matrix):
	result = ""
	if len(s) % 2 == 0:
		plain = s
	else:
		plain = s + "n5vgru7ehz1klja8s9340m2wcxbd6pqfitoy"[0]
	for i in range(0, len(plain), 2):
		result += encrypt_pair(plain[i:i + 2], matrix)
	return result

alphabet = open("key").read().rstrip()
m = generate_square(alphabet)
msg = open("msg").read().rstrip()
enc_msg = encrypt_string(msg, m)
print("Here is the alphabet: {}\nHere is the encrypted message: {}".format(alphabet, enc_msg))
signal.alarm(18)
resp = input("What is the plaintext message? ").rstrip()
if resp and resp == msg:
	print("Congratulations! Here's the flag: {}".format(open("flag").read()))

# https://en.wikipedia.org/wiki/Playfair_cipher

```
Creamos un programa que lo decripte:
```python
SQUARE_SIZE = 6
def generate_square(alphabet):
        assert len(alphabet) == pow(SQUARE_SIZE, 2) #can be ignored here
        matrix = []
        for i, letter in enumerate(alphabet):
                if i % SQUARE_SIZE == 0: #i%6==0
                        row = []
                row.append(letter)
                if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
                        matrix.append(row)
        return matrix

def get_index(letter, matrix):
        for row in range(SQUARE_SIZE):
                for col in range(SQUARE_SIZE):
                        if matrix[row][col] == letter:
                                return (row, col)
        print("letter not found in matrix.")
        exit()

def decrypt_pair(pair, matrix):
        #print("pair=",pair)
        p1 = get_index(pair[0], matrix) #(row,col)
        p2 = get_index(pair[1], matrix) #(row,col)

        if p1[0] == p2[0]: #same row
                return matrix[p1[0]][(p1[1] - 1)  % SQUARE_SIZE] + matrix[p2[0]][(p2[1] - 1)  % SQUARE_SIZE]
        elif p1[1] == p2[1]: #same col
                return matrix[(p1[0] - 1)  % SQUARE_SIZE][p1[1]] + matrix[(p2[0] - 1)  % SQUARE_SIZE][p2[1]]
        else: #neither
                return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]

def decrypt_string(s, matrix):
        result = ""
        for i in range(0, len(s), 2):
                print("now i=",i)
                result += decrypt_pair(s[i:i + 2], matrix)
        return result

alphabet = input("Alphabet: ")
m = generate_square(alphabet) #key table
enc_msg=input("Ecnripted: ")
msg=decrypt_string(enc_msg,m)
print(msg)
```
Y lo ejecutamos con los datos que nos dan en ncat, luego pasamos el resultado a ncat y nos da la flag:
```bash
❯ nc mercury.picoctf.net 19354
Here is the alphabet: n5vgru7ehz1klja8s9340m2wcxbd6pqfitoy
Here is the encrypted message: hnjm2e4t51v16gsg104i4oi9wmrqli
What is the plaintext message? ^C

❯ python3 solve.py
Alphabet: n5vgru7ehz1klja8s9340m2wcxbd6pqfitoy
Ecnripted: hnjm2e4t51v16gsg104i4oi9wmrqli
now i= 0
now i= 2
now i= 4
now i= 6
now i= 8
now i= 10
now i= 12
now i= 14
now i= 16
now i= 18
now i= 20
now i= 22
now i= 24
now i= 26
now i= 28
7v8441mfrerhdr8rh20f2fya20noaq
❯ nc mercury.picoctf.net 19354
Here is the alphabet: n5vgru7ehz1klja8s9340m2wcxbd6pqfitoy
Here is the encrypted message: hnjm2e4t51v16gsg104i4oi9wmrqli
What is the plaintext message? 7v8441mfrerhdr8rh20f2fya20noaq
Congratulations! Here's the flag: dbc8bf9bae7152d35d3c200c46a0fa30
```
Siendo la flag la siguiente:
dbc8bf9bae7152d35d3c200c46a0fa30
## Notas Adicionales


## Referencias
