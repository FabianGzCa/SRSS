## Objetivo
Deberemos encontrar la contraseña en el archivo `data.txt`, que es un volcado hexadecimal (hexdump) de un archivo que ha sido comprimido repetidamente. Primero, se recomienda crear un directorio temporal usando `mktemp -d`, luego copiar y renombrar el archivo. Usaremos `xxd` para convertir el volcado hexadecimal de vuelta a un archivo binario y descomprimiremos el archivo sucesivamente hasta obtener la contraseña.

## Datos de Acceso al Nivel
 **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit2
- **contraseña:** 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

## Solución
```bash
ls -l
```
```text
total 4
-rw-r----- 1 bandit13 bandit12 2638 Jul 17 15:57 data.txt
```
```bash
xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | zcat
```
```text
total 4
The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
```

## Notas Adicionales
El comando usado convierte el archivo data.txt que está en hexadecimal de un archivo comprimido varias veces en su forma original, descomprimiéndolo repetidamente a través de varios formatos de compresión.

## Referencias