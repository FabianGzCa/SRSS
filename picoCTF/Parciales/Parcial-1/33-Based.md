## Objetivo
To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with `nc jupiter.challenges.picoctf.org 15130`.

## Solución
```bash
nano base.py
tipo = int(input("Base (2 para binario, 8 para octal, 16 para hexadecimal): "))

cadena = input("Descifrar: ")

if tipo == 2:
    numeros = cadena.split()
    decimales = [int(num, 2) for num in numeros]
    resultado = ''.join(chr(d) for d in decimales)

elif tipo == 8:
    numeros = cadena.split()
    decimales = [int(num, 8) for num in numeros]
    resultado = ''.join(chr(d) for d in decimales)

elif tipo == 16:
    resultado = bytes.fromhex(cadena).decode('ascii')

else:
    print("Base no soportada.")
    resultado = ""

print("Texto resultante:", resultado)

nc jupiter.challenges.picoctf.org 15130
Let us see how data is stored
lizard
Please give the 01101100 01101001 01111010 01100001 01110010 01100100 as a word.
...
you have 45 seconds.....

Input:
lizard
Please give me the  163 157 143 153 145 164 as a word.
Input:
socket
Please give me the 736c75646765 as a word.
Input:
sludge
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_02167de8}

```

## Notas Adicionales


## Referencias
