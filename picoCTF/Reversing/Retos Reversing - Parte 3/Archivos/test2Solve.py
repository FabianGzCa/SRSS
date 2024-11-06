# Valores iniciales
e4 = int('0x21', 16)  # Inicialización de ebp-0x4
e8 = int('0x4', 16)   # Inicialización de ebp-0x8

# Ciclo hasta que e8 supere el límite de 0xfb46
while e8 <= int('0xfb46', 16):
    e4 += int('0x1', 16)    # Incremento de ebp-0x4
    e8 += int('0x74', 16)   # Incremento de ebp-0x8

# Resultado final en formato hexadecimal
print(hex(e4))
