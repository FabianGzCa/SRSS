## Objetivo
Encontrar la contraseña almacenada en un archivo llamado `-` ubicado en el directorio principal.

## Datos de Acceso al Nivel
* **comando:** ssh
* **host:** bandit.labs.overthewire.org
* **puerto:** 2220
* **usuario:** bandit1
* **contraseña:** ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

## Solución
```bash
ls
```
```text
-
```
```bash
cat ./-
```
```text
263JGJPfgU6LtdEvgfWU1XP5yac29mFx
```
## Notas Adicionales
El directorio `-` no puede ser leído directamente con `cat -` debido a que, al igual que en la mayoría de comandos, `cat` utiliza el `-` para leer la entrada estándar. Por lo que se debe especificar la ruta del archivo con `./archivo`, que en este caso es `./-`.

## Referencias