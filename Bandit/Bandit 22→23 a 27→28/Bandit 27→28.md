## Objetivo
Deberemos clonar un repositorio Git ubicado en `ssh://bandit27-git@localhost/home/bandit27-git/repo` a través del puerto 2220. La contraseña para el usuario `bandit27-git` es la misma que la del usuario `bandit27`.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit27
- **contraseña:** upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB

## Solución
```bash
mktemp -d
```
```text
/tmp/tmp.oUpij4PYb1
```
```bash
cd /tmp/tmp.oUpij4PYb1
git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
```
```text
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit27/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit27-git@localhost's password: 
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
```
```bash
ls -la
```
```text
total 10816
drwx------    3 bandit27 bandit27     4096 Sep  7 06:16 .
drwxrwx-wt 6894 root     root     11063296 Sep  7 06:17 ..
drwxrwxr-x    3 bandit27 bandit27     4096 Sep  7 06:17 repo
```
```bash
cd repo/
ls -la
```
```text
total 16
drwxrwxr-x 3 bandit27 bandit27 4096 Sep  7 06:17 .
drwx------ 3 bandit27 bandit27 4096 Sep  7 06:16 ..
drwxrwxr-x 8 bandit27 bandit27 4096 Sep  7 06:17 .git
-rw-rw-r-- 1 bandit27 bandit27   68 Sep  7 06:17 README
```
```bash
cat README
```
```text
The password to the next level is: Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN
```

## Notas Adicionales


## Referencias