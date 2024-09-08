## Objetivo
Debemos clonar el repositorio Git en `ssh://bandit30-git@localhost/home/bandit30-git/repo` a través del puerto 2220. La contraseña para el usuario `bandit30-git` es la misma que la de `bandit30`. Una vez clonado el repositorio, exploraremos su contenido para encontrar la contraseña para el siguiente nivel.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit30
- **contraseña:** qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL

## Solución
```bash
bandit30@bandit:~$ mktemp -d
/tmp/tmp.gIQokRPjHy
bandit30@bandit:~$ cd /tmp/tmp.gIQokRPjHy
bandit30@bandit:/tmp/tmp.gIQokRPjHy$ git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit30/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit30/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit30-git@localhost's password: 
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
bandit30@bandit:/tmp/tmp.gIQokRPjHy$ cd repo/
bandit30@bandit:/tmp/tmp.gIQokRPjHy/repo$ cat README.md 
just an epmty file... muahaha
bandit30@bandit:/tmp/tmp.gIQokRPjHy/repo$ git tag
WARNING: terminal is not fully functional
Press RETURN to continue 
secret
bandit30@bandit:/tmp/tmp.gIQokRPjHy/repo$ git show secret
WARNING: terminal is not fully functional
Press RETURN to continue 
fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy
```

## Notas Adicionales


## Referencias