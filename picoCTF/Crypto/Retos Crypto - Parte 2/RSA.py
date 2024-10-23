from gmpy2 import *

get_context().precision = 2048

n = mpz(input("Ingresa el valor de n: "))
e = 3
c = mpz(input("Ingresa el valor de c: "))

for attempt in range(10000):
    m, exact = iroot(attempt * n + c, e)
    if exact:
        print(f'T encontrado: {attempt}')
        print(f'Mensaje: {bytes.fromhex(hex(m)[2:]).decode()}')
