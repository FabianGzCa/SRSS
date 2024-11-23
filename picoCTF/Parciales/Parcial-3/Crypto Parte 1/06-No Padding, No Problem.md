## Objetivo
Oracles can be your best friend, they will decrypt anything, except the flag's ciphertext. How will you break it? Connect with `nc mercury.picoctf.net 2671`.

## Solución
Nos conectamos al ncat que nos da y recibimos esto:
```bash
❯ nc mercury.picoctf.net 2671
Welcome to the Padding Oracle Challenge
This oracle will take anything you give it and decrypt using RSA. It will not accept the ciphertext with the secret message... Good Luck!


n: 154193208276236320288874774262536820007969541666633088027605878059003685521718563221031805904728588849468024133010179936301157439382632282219409441997121304742314827768180137574101135641402382209886551558990261191411737500656205810001787686028851450958037210207126749293033234100174337001801046792136276168379
e: 65537
ciphertext: 37559906556918882320130554390083224174035497143698571211541296916660229724122065120407762440889406599673501104920084328279150503499279886995139611193411183834122475957752965657774542727562167155606957062269071312435585784515394182136405801859713238260853249317362274105584745873959374185608398108021960071216


Give me ciphertext to decrypt: 
```
Entonces creamos un código de python que lo resuelva:
```python
from pwn import *
import binascii

r = remote('mercury.picoctf.net', 2671)
r.recvlines(4)

r.recvuntil(b'n: ')
n = int(r.recvline().strip())

r.recvuntil(b'e: ')
e = int(r.recvline().strip())

r.recvuntil(b'ciphertext: ')
c = int(r.recvline().strip())

payload = c * pow(2,e,n)
r.sendlineafter(b'Give me ciphertext to decrypt: ', str(payload))

r.recvuntil(b'Here you go: ')
doubled_plain = int(r.recvline().strip())
print("Doubled Plain:", doubled_plain)

plain_hex = hex(doubled_plain // 2)[2:]
plain_bytes = bytes.fromhex(plain_hex)
print("Plain Text Hex:", plain_hex)
print("Plain Text:", plain_bytes.decode())

r.close()
```
Y lo ejecutamos:
```python
❯ python3 solve.py
[+] Opening connection to mercury.picoctf.net on port 2671: Done
/home/fabiangzca/Documents/Escuela/SRSS/picoCTF/Parciales/Parcial-3/Crypto Parte 1/Archivos/solve.py:17: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  r.sendlineafter(b'Give me ciphertext to decrypt: ', str(payload))
Doubled Plain: 580550060391700078946913236734911770139931497702556153513487440893406629034802718534645538074938502890769430290200460554490
Plain Text Hex: 7069636f4354467b6d347962335f54683073655f6d337335346733735f3472335f646966757272656e745f353831343336387d
Plain Text: picoCTF{m4yb3_Th0se_m3s54g3s_4r3_difurrent_5814368}
[*] Closed connection to mercury.picoctf.net port 2671
```
dandonos la respuesta:
picoCTF{m4yb3_Th0se_m3s54g3s_4r3_difurrent_5814368}
## Notas Adicionales


## Referencias
