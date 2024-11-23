2## Objetivo
I just recently learnt about the SRA public key cryptosystem... or wait, was it supposed to be RSA? Hmmm, I should probably check...

## Solución
Revisamos el archivo que nos dan:
```bash
❯ catn chal.py
from Crypto.Util.number import getPrime, inverse, bytes_to_long
from string import ascii_letters, digits
from random import choice

pride = "".join(choice(ascii_letters + digits) for _ in range(16))
gluttony = getPrime(128)
greed = getPrime(128)
lust = gluttony * greed
sloth = 65537
envy = inverse(sloth, (gluttony - 1) * (greed - 1))

anger = pow(bytes_to_long(pride.encode()), sloth, lust)

print(f"{anger = }")
print(f"{envy = }")

print("vainglory?")
vainglory = input("> ").strip()

if vainglory == pride:
    print("Conquered!")
    with open("/challenge/flag.txt") as f:
        print(f.read())
else:
    print("Hubris!")
```
Tenemos un texto cifrado y el valor de _d_, pero no conocemos _n_. Sabemos que e⋅dmod  (p−1)(q−1)=1e \cdot d \mod (p-1)(q-1) = 1e⋅dmod(p−1)(q−1)=1, y que _p_ y _q_ son primos de 128 bits. A partir de esto, generamos una lista de posibles valores para _p_ y _q_, y probamos descifrar usando cada valor de _n_. El resultado que da un texto legible es el correcto, y finalmente el programa nos revela la bandera.


creamos un archivo que resuelva el problema:
```python
from pwn import *
import primefac
from itertools import combinations
from Crypto.Util.number import long_to_bytes

#function to generate all the sub lists
def sub_lists (l):
    #initializing empty list
    comb = []

    #Iterating till length of list
    for i in range(1,len(l)+1):
        #Generating sub list
        comb += [list(j) for j in combinations(l, i)]
    #Returning list
    return comb

def divisors(phi):
   print("Give me the divisors of ", phi-1)
   #this is dangerous, but I'm trusting me
   return(eval(input()))

#connect to the server
r = remote('saturn.picoctf.net', 64954)
#get ciphertext
r.recvuntil("anger =")
ciphertext=int(r.recvline())
#get d
r.recvuntil("envy =")
d=int(r.recvline())
print("cipher=",ciphertext)
print("d=",d)
print(r.recvuntil("vainglory?"))
r.recvline()
#since d is e^-1 mod (p-1)*(q-1), d*e=k*(p-1)*(q-1)+1
#so (p-1)*(q-1)*k = d*e-1
factors=divisors(d*65537)
combos = sub_lists(factors)
primes = set()
#try all possible subsets of the list of factors as the factors of (p-1)
for l in combos:
   product = 1
   #multiply them together to get p-1
   for k in l:
      product = product * k
   #if the right length and adding 1 yields a prime, then maybe
   if product.bit_length()==128 and primefac.isprime(product+1):
      primes.add(product+1)
print(primes)
primelist = list(primes)
#try all possible prime pairs
for p in primelist:
   for q in primelist:
      n=p*q
      #decode with this possible n
      plain = pow(ciphertext,d,n)
      try:
         plaintext = long_to_bytes(plain)
         #see if it corresponds to text and if so, try it
         print(plaintext.decode())
         r.sendline(plaintext.decode())
         print(r.recvline())
         print(r.recvline())
         print(r.recvline())
      except:
         continue
```
Lo ejecutamos y nos pide divisores:
```bash
❯ python3 solve2.py
[+] Opening connection to saturn.picoctf.net on port 64511: Done
/home/fabiangzca/Documents/Escuela/SRSS/picoCTF/Parciales/Parcial-3/Crypto Parte 2/Archivos/solve2.py:27: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  r.recvuntil("anger =")
/home/fabiangzca/Documents/Escuela/SRSS/picoCTF/Parciales/Parcial-3/Crypto Parte 2/Archivos/solve2.py:30: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  r.recvuntil("envy =")
cipher= 27960152487344864275800723250570493882054263363872114622827080490504798207884
d= 5758871449787647563646064223621970481582475208958498121452215393316813098313
/home/fabiangzca/Documents/Escuela/SRSS/picoCTF/Parciales/Parcial-3/Crypto Parte 2/Archivos/solve2.py:34: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  print(r.recvuntil("vainglory?"))
b'vainglory?'
Give me the divisors of  377419158204733058378672111023513079451470677769513091385613840231803980024139080
```
y en pagina de dcode.fr descomponemos el número que nos dan para obtener la respuesta y la flag
## Notas Adicionales


## Referencias
https://www.dcode.fr/prime-factors-decomposition