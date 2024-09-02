## Objetivo
Encontrar la contraseña almacenada en el único archivo legible por humanos en el directorio `inhere`.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit4
- **contraseña:** 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

## Solución
```bash
ls -l
```
```text
drwxr-xr-x 2 root root 4096 Jul 17 15:57 inhere
```
```bash
cd inhere/
file ./*
``````
```text
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
```
```bash
cat ./-file07
```
## Notas Adicionales
#### Comandos:
* **file {archivo}** :  Determina y muestra el tipo de archivo, indicando si es texto, binario, etc.
En el caso del comando utilizado, `file ./*`, el `*` representa todos los archivos del directorio actual, por lo que lo ejecuta para cada uno de ellos.
## Referencias