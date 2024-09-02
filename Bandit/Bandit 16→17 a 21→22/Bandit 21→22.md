## Objetivo
Deberemos examinar la configuración del programador de tareas basado en tiempo, cron, ubicado en el directorio `/etc/cron.d/`, para identificar qué comando específico se está ejecutando automáticamente en intervalos regulares. Esto implicará revisar los archivos de configuración de cron y entender su contenido. Para lograrlo, podremos utilizar comandos como `cron`, `crontab` y consultar la página de manual de `crontab(5)` con la finalidad de comprender cómo está estructurada la programación y ejecución de tareas en el sistema.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit21
- **contraseña:** EeoULMCra2q0dSkYj561DX7s1CpBuOBt

## Solución
```bash
cd /etc/cron.d/
ls -l
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
cat cronjob_bandit22
```
```text
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
```
```bash
cd /usr/bin/
./cronjob_bandit22.sh
```
```text
chmod: changing permissions of '/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv': Operation not permitted
./cronjob_bandit22.sh: line 3: /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv: Permission denied
```
```bash
cd /tmp/
cat t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```
```text
tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
```

## Notas Adicionales
los cron se ejecutaran en un intervalo de tiempo

## Referencias