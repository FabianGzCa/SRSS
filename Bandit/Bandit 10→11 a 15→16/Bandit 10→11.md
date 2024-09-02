## Objetivo
Deberemos encontrar la contraseña en el archivo `data.txt`, que contiene datos codificados en base64. Para obtener la contraseña, se deberá decodificar el contenido del archivo utilizando el comando `base64`.

## Datos de Acceso al Nivel
 **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit10
- **contraseña:** FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

## Solución
```bash
ls -l
```
```text
total 4
-rw-r----- 1 bandit11 bandit10 69 Jul 17 15:57 data.txt
```
```bash
base64 -d data.txt
```
```text
The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
```
## Notas Adicionales
Decodificamos el contenido de data.txt que estaba en base 64.

## Referencias