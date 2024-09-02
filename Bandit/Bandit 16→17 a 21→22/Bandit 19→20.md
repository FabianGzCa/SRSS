## Objetivo
Deberemos utilizar un binario setuid ubicado en el directorio personal para obtener acceso al siguiente nivel. Primero, ejecutaremos el binario sin argumentos para descubrir cómo se utiliza. Luego, aplicaremos el conocimiento obtenido para acceder a la contraseña del nivel actual, que se encuentra en la ubicación habitual (`/etc/bandit_pass`). Para completar esta tarea, es recomendable comprender el funcionamiento del bit setuid, que podemos revisar en la documentación o en fuentes como Wikipedia.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit19
- **contraseña:** cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8

## Solución
```bash
ls -l
```
```text
total 16
-rwsr-x--- 1 bandit20 bandit19 14880 Jul 17 15:57 bandit20-do
```
```bash
./bandit20-do cat /etc/bandit_pass/bandit20
```
```text
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
```

## Notas Adicionales
el binario bandit20-do ejecuta el comando que se le pasa como argumento

## Referencias