## Objetivo
We have recovered a [binary](https://jupiter.challenges.picoctf.org/static/48babf8f8c4c6b8baf336680ea5b9ddf/rev) and a [text file](https://jupiter.challenges.picoctf.org/static/48babf8f8c4c6b8baf336680ea5b9ddf/rev_this). Can you reverse the flag.

## Solución
Revisamos información de los archivos dados:
```bash
❯ file rev
rev: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=523d51973c11197605c76f84d4afb0fe9e59338c, not stripped
❯ file rev_this
rev_this: ASCII text, with no line terminators
```
abrimos el archivo rev con ghidra donde analizando el código encontramos la zona de encriptación:

```cpp
  for (j = 8; (int)j < 0x17; j = j + 1) {
    if ((j & 1) == 0) {
      rev = flag[(int)j] + '\x05';
    }
    else {
      rev = flag[(int)j] + -2;
    }
    fputc((int)rev,flag_rev);
  }
  ```
  Así que creamos un código de python para hacer el proceso inverso:
  ```python
catn exp.py
cifrado = open("rev_this", "r").read()

print(cifrado)

flag = ""

for i in range(8, len(cifrado)-1):
        if (i & 1 == 0):
                flag += chr( ord(cifrado[i])-5 )
        else:
                flag += chr( ord(cifrado[i])+2 )

print (flag)
```
que nos da lo que va dentro de picoCTF{}
teniendo la flag:
picoCTF{r3v3rs312528e05}

## Notas Adicionales


## Referencias
