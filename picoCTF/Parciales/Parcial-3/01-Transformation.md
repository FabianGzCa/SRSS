## Objetivo
I wonder what this really is... [enc](https://mercury.picoctf.net/static/e47483f88b12f2ab0c46315afc12f64d/enc) `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`

## Solución
Revisamos el archivo que nos dan:
```bash
❯ catn enc
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽%   
```
Creamos un programa en python para descifrar el texto:
```python
encoded_flag = open("enc").read()
flag = ""
for i in range(0, len(encoded_flag)):
    character1 = chr((ord(encoded_flag[i]) >> 8))
    character2 = chr(encoded_flag[i].encode('utf-16be')[-1])
    flag += character1
    flag += character2

print("Flag: " + flag)
```
y al ejecutarlo nos da la flag:
```bash
❯ python3 solve.py
Flag: picoCTF{16_bits_inst34d_of_8_e141a0f7}
```

## Notas Adicionales


## Referencias
