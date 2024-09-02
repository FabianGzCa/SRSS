## Objetivo
Deberemos interactuar con un binario setuid ubicado en el directorio personal, que se conecta a un puerto local especificado como argumento en la línea de comandos. El binario leerá una línea de texto de la conexión y la comparará con la contraseña del nivel anterior (bandit20). Si la contraseña es correcta, el binario enviará la contraseña para el siguiente nivel (bandit21). Para lograrlo, intentaremos conectarnos a nuestro propio demonio de red utilizando comandos como `nc`, y exploraremos opciones como `ssh`, `cat`, `bash`, `screen`, `tmux`, y técnicas de control de trabajos en Unix para verificar que el proceso funcione según lo esperado.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit20
- **contraseña:** 

## Solución
```bash
nc -lnvp 9000 <<< 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO &
```
```text
[3] 3129020
bandit20@bandit:~$ Listening on 0.0.0.0 9000
```
```bash
teclear CTRL + Z
```
```bash
./suconnect 9000
```
```text
Connection received on 127.0.0.1 54874
Read: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
Password matches, sending next password
EeoULMCra2q0dSkYj561DX7s1CpBuOBt
[3]+  Done                    nc -lnvp 9000 <<< 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
```

## Notas Adicionales
Nos ponemos en escucha en el puerto 9000 con la llave del usuario actual para que el binario pueda funcionar mandandole una conexión a ese puerto

## Referencias