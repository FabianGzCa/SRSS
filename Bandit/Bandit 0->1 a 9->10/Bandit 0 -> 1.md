## Objetivo
Encontrar la contraseña almacenada en el archivo readme que se ubica en el directorio principal para poder acceder al usuario bandit1 mediante SSH en el puerto 2220.
## Datos de Acceso al Nivel
* **comando:** ssh
* **host:** bandit.labs.overthewire.org
* **puerto:** 2220
* **usuario:** bandit0
* **contraseña:** bandit0

## Solución

```bash
bandit0@bandit:~$ ls
```
```text
readme
```
```bash
bandit0@bandit:~$ cat readme
```
```text
Congratulations on your first steps into the bandit game!!
Please make sure you have read the rules at https://overthewire.org/rules/
If you are following a course, workshop, walthrough or other educational activity,
please inform the instructor about the rules as well and encourage them to
contribute to the OverTheWire community so we can keep these games free!

The password you are looking for is: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
```
## Notas Adicionales
#### Comandos:
* **ls** :  Muestra el contenido del directorio en el que se encuentra.
* **cat {archivo}** : Muestra el contenido de {archivo}
## Referencias