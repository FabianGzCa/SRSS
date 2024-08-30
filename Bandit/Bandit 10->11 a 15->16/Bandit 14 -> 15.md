## Objetivo
Deberemos recuperar la contraseña para el siguiente nivel enviando la contraseña del nivel actual al puerto 30000 en `localhost`. Para realizar esto, podemos usar el comando `nc` (netcat) para conectar al puerto especificado y enviar la contraseña.

## Datos de Acceso al Nivel
 **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit2
- **contraseña:** MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS

## Solución
```bash
nc localhost 30000
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
```
```text
Correct!
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```


## Notas Adicionales
Utilizamos ncat para conectarnos al servicio que corre en el puerto 30000 en el localhost el cual nos solicita una contraseña, colocamos la de inicio a bandit 14.

## Referencias