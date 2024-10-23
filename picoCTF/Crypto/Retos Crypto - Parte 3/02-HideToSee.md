## Objetivo
How about some hide and seek heh? Look at this image [here](https://artifacts.picoctf.net/c/240/atbash.jpg).

## Solución
Nos dan una imagen, utilizamos el comando
`steghide extract -sf atbash.jpg`
sin contraseña y nos da el siguiente valor:
krxlXGU{zgyzhs_xizxp_xz00558y}
que tiene el formato de una flag, vamos a desencriptarlo en una página 
y al meter nuestro valor nos regresa la flag:
picoCTF{atbash_crack_ca00558b}


## Notas Adicionales


## Referencias
https://www.dcode.fr/atbash-cipher?__r=1.cfecb5bbe7c7da3000ac747b60b5d75c