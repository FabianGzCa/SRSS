## Objetivo
Deberemos investigar el programa que se ejecuta automáticamente a intervalos regulares mediante el uso de cron, el planificador de trabajos basado en tiempo. Para hacerlo, revisaremos la configuración en el directorio `/etc/cron.d/` para identificar qué comando específico está siendo ejecutado. El script asociado a este nivel está diseñado para ser fácil de leer, por lo que si encontramos dificultades para entender su funcionamiento, podemos ejecutarlo para ver la información de depuración que imprime.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit22
- **contraseña:** tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q

## Solución
```bash
ls -l /etc/cron.d
```
```text
total 24
-rw-r--r-- 1 root root 120 Jul 17 15:57 cronjob_bandit22
-rw-r--r-- 1 root root 122 Jul 17 15:57 cronjob_bandit23
-rw-r--r-- 1 root root 120 Jul 17 15:57 cronjob_bandit24
-rw-r--r-- 1 root root 201 Apr  8 14:38 e2scrub_all
-rwx------ 1 root root  52 Jul 17 15:59 otw-tmp-dir
-rw-r--r-- 1 root root 396 Jan  9  2024 sysstat
```
```bash
cat /etc/cron.d/cronjob_bandit23
```
```text
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null```text
```
```bash
cat /usr/bin/cronjob_bandit23.sh
```
```bash
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```
```bash
echo $(echo I am user bandit23 | md5sum | cut -d ' ' -f 1)
```
```text
8ca319486bfbbc3663ea0fbe81326349
```
```bash
cat /tmp/8ca319486bfbbc3663ea0fbe81326349
```
```text
0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
```

## Notas Adicionales


## Referencias