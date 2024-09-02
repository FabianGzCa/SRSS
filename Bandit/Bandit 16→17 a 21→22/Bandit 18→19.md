## Objetivo
Deberemos recuperar la contraseña para el siguiente nivel, la cual está almacenada en un archivo llamado `readme` en el directorio personal. Sin embargo, el archivo `.bashrc` ha sido modificado para desconectarte automáticamente al iniciar sesión a través de SSH. Por lo tanto, primero necesitaremos encontrar una manera de evitar el logout automático para poder acceder al archivo `readme`. Utilizaremos comandos como `ssh`, `ls` y `cat` para listar los archivos y leer el contenido del archivo `readme` una vez que estemos en el directorio adecuado.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit18
- **contraseña:** x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO

## Solución
```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 ls -l
```
```text
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

total 4
-rw-r----- 1 bandit19 bandit18 33 Jul 17 15:57 readme
```
```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
```
```text
cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
```

## Notas Adicionales
con ssh podemos ejecutar comandos si nos podemos conectar colocando el comando al final de la conexión ssh

## Referencias