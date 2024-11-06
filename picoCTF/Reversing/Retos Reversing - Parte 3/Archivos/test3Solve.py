# Valores de entrada
param1 = 0xba6c5a02
param2 = 0xd101e3dd
param3 = 0xbb86a173

# Paso 1: Inicialización
a = 0

# Paso 2: mov ah, BYTE PTR [ebp+0xa]
# Esto toma el byte en la posición 0x0A de param1 (que es el tercer byte de param1)
a |= ((param1 & 0x00FF0000) >> 16) << 8  # Extraemos el byte '0x5a' y lo colocamos en 'ah'

# Paso 3: shl ax, 0x10
a <<= 16  # Desplaza ax 16 bits hacia la izquierda, colocando el valor en los bits más significativos de eax

# Paso 4: sub al, BYTE PTR [ebp+0xf]
# Esto toma el byte en la posición 0x0F de param2 (que es el primer byte de param2)
a = (a & 0xFFFFFF00) | ((a & 0xFF) - ((param2 & 0xFF000000) >> 24) & 0xFF)

# Paso 5: add ah, BYTE PTR [ebp+0xe]
# Esto suma el segundo byte de param2 a 'ah'
a = (a & 0xFFFF00FF) | (((((a & 0xFFFF00FF) >> 8) + ((param2 & 0x00FF0000) >> 16)) & 0xFF) << 8)

# Paso 6: xor ax, WORD PTR [ebp+0x12]
# Esto realiza XOR entre ax y los últimos 16 bits de param3
a ^= (param3 & 0x0000FFFF)

# Resultado final
print(hex(a))
