## Objetivo
Encontrar la contraseña almacenada en un archivo bajo el directorio `inhere` que sea legible por humanos, tenga un tamaño de 1033 bytes y no sea ejecutable.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit5
- **contraseña:** 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

## Solución
```bash
ls -l
```
```text
drwxr-xr-x 2 root root 4096 Jul 17 15:57 inhere
```
```bash
find inhere/ -type f -readable -size 1033c ! -executable
```
```text
inhere/maybehere07/.file2
```
```bash
cat inhere/maybehere07/.file2
```
```text
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
```
## Notas Adicionales
Dentro del comando `find`, `-type f` nos ayuda a obtener resultados de tipo archivo, es decir, solo archivos. El `-readable` filtra para mostrar solo archivos que podemos leer, `-size {number}c` filtra los archivos que tengan exactamente **number** bytes (la medida se especifica con la c), y el `! -executable` excluye todos los archivos que sean ejecutables del resultado final.


## Referencias