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
