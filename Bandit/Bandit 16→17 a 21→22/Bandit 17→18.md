## Objetivo
Deberemos identificar la contraseña para el siguiente nivel, que se encuentra en el archivo `passwords.new` y es la única línea que ha cambiado en comparación con el archivo `passwords.old`. Para ello, utilizaremos comandos como `diff` para comparar los dos archivos y detectar las diferencias, y comandos como `cat` y `grep` para examinar el contenido de los archivos y encontrar la línea modificada. Asegúrate de revisar el archivo `passwords.new` para extraer la contraseña correcta. Ten en cuenta que si encuentras el mensaje ‘Byebye!’ al intentar iniciar sesión en `bandit18`, esto está relacionado con el siguiente nivel, `bandit19`.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit17
- **contraseña:** EReVavePLFHtFlFsjn3hyzMlvSuSAcRD

## Solución
```bash
ls -l
```
```text
total 8
-rw-r----- 1 bandit18 bandit17 3300 Jul 17 15:57 passwords.new
-rw-r----- 1 bandit18 bandit17 3300 Jul 17 15:57 passwords.old
```
```bash
diff passwords.new passwords.old
```
```text
42c42
< bSrACvJvvBSxEM2SGsV5sn09vc3xgqyp
---
> x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
```

## Notas Adicionales
vemos la diferencia entre 2 archivos con el comando diff

## Referencias