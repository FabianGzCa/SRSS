## Objetivo
Encontrar la contraseña almacenada en un archivo oculto ubicado en el directorio `inhere`.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit2
- **contraseña:** MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
## Solución
```bash
ls -l
```
```text
total 4
drwxr-xr-x 2 root root 4096 Jul 17 15:57 inhere
```
```bash
cd inhere/
ls -a
```
```text
.  ..  ...Hiding-From-You
```
```bash
cat ...Hiding-From-You
```
```text
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
```
## Notas Adicionales
#### Comandos:
* **ls -l** :  Muestra una lista detallada del contenido del directorio, donde si la primer letra es la **d** sabremos que es un directorio.
* **ls -a** : Muestra todos los archivos, incluidos los ocultos.

## Referencias