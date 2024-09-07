## Objetivo
deberemos explorar el sistema de archivos o el entorno del usuario `bandit26` para localizar el archivo que contiene la contraseña para `bandit27`. Utiliza comandos y herramientas estándar como `ls`, `cat`, `more`, `find`, o `grep` para buscar y acceder a la información necesaria. ¡Asegúrate de realizar una búsqueda exhaustiva en los directorios y archivos del usuario para encontrar la contraseña!
## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit26
- **contraseña:** s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ

## Solución

```text
v
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
:set shell=/bin/bash
:shell
```
```bash
ls
```
```text
bandit27-do text.txt
```
```bash
./bandit27-do cat /etc/bandit_pass/bandit27
```
```text
upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB
```

## Notas Adicionales
Se necesita reducir el tamaño la terminal para que funcione.

## Referencias