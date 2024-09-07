## Objetivo
Deberemos iniciar sesión en `bandit26` desde `bandit25`, pero el shell para el usuario `bandit26` no es `/bin/bash` sino que es otro tipo de shell. El desafío consiste en identificar qué shell se está utilizando, comprender su funcionamiento y encontrar una forma de salir de él para obtener acceso al sistema como `bandit26`.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit25
- **contraseña:** iCi86ttT4KSNe1armKiwbQNmB3YJP3q4

## Solución
```bash
ls -l
```
```text
total 4
-r-------- 1 bandit25 bandit25 1679 Jul 17 15:57 bandit26.sshkey
```
```bash
ssh -i bandit26.sshkey bandit26@localhost -p2220
```
```text
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit25/.ssh' (Permission denied).
Failed to add the host to the list of known hosts 
v
(/home/bandit25/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
:e /etc/bandit_pass/bandit26
s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
:q!
```


## Notas Adicionales
Se necesita reducir el tamaño la terminal para que funcione.

## Referencias