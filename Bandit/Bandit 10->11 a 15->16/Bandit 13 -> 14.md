## Objetivo
Deberemos encontrar la contraseña para el siguiente nivel en el archivo `/etc/bandit_pass/bandit14`, al que solo puede acceder el usuario `bandit14`. Para ello, se nos proporciona una clave SSH privada que se debe usar para iniciar sesión en el siguiente nivel. La conexión se realiza a `localhost`, que se refiere a la máquina en la que estamos trabajando. Para conectarnos, utilizaremos el comando `ssh` con la clave proporcionada.

## Datos de Acceso al Nivel
 **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit2
- **contraseña:** FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn

## Solución
```bash
total 4
-rw-r----- 1 bandit14 bandit13 1679 Jul 17 15:57 sshkey.private
```
```text
total 4
-rw-r----- 1 bandit13 bandit12 2638 Jul 17 15:57 data.txt
```
```bash
ssh -i sshkey.private bandit14@localhost -p 2220
```

## Notas Adicionales
Nos conectamos via ssh con una llave privada a localhost en el usuario bandit14 por el puerto 2220

## Referencias