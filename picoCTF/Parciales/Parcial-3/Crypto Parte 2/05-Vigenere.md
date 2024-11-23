## Objetivo
Can you decrypt this message?Decrypt this [message](https://artifacts.picoctf.net/c/159/cipher.txt) using this key "CYLAB".

## Solución
Revisamos el contenido del archivo:
```bash
catn cipher.txt
rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_f85729e7}
```
Y metemos la salida a cyberchef con el formato de Vigenere Decode con la clave CYLAB regresandonos la flag:
picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_d85729g7}

## Notas Adicionales


## Referencias
