## Objetivo
Encontrar la contraseña almacenada en un archivo llamado `spaces in this filename` ubicado en el directorio principal.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit2
- **contraseña:** 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

## Solución
```bash
ls
```
```text
spaces in this filename
```
```bash
cat spaces\ in\ this\ filename
```
```text
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
```

## Notas Adicionales
Hemos utilizado el `\` antes de los espacios para escaparlos, es decir, para que la terminal no los interprete como espacios sino como texto. Aunque, dado que no es un carácter especial que realiza acciones, también podemos hacer uso de las comillas para encapsular el nombre del archivo de la siguiente manera: `cat "spaces in this filename"`.
## Referencias