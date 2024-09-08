## Objetivo
Debemos clonar el repositorio Git en `ssh://bandit31-git@localhost/home/bandit31-git/repo` utilizando el puerto 2220. La contraseña para el usuario `bandit31-git` es la misma que para el usuario `bandit31`. Una vez clonado el repositorio, exploraremos su contenido para encontrar la contraseña del siguiente nivel.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit31
- **contraseña:** fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy

## Solución
```bash
bandit31@bandit:~$ mktemp -d
/tmp/tmp.lmx9akaUcD
bandit31@bandit:~$ cd /tmp/tmp.lmx9akaUcD
bandit31@bandit:/tmp/tmp.lmx9akaUcD$ git clone ssh://bandit31-git@localhost:2220ome/bandit31-git/repo
Cloning into 'repo'...
ssh: Could not resolve hostname localhost:2220ome: Name or service not known
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
bandit31@bandit:/tmp/tmp.lmx9akaUcD$ ls
bandit31@bandit:/tmp/tmp.lmx9akaUcD$ git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo 
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit31/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit31/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit31-git@localhost's password: 
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
bandit31@bandit:/tmp/tmp.lmx9akaUcD$ cd repo/
bandit31@bandit:/tmp/tmp.lmx9akaUcD/repo$ ls
README.md
bandit31@bandit:/tmp/tmp.lmx9akaUcD/repo$ cat README.md 
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master

bandit31@bandit:/tmp/tmp.lmx9akaUcD/repo$ nano key.txt
Unable to create directory /home/bandit31/.local/share/nano/: No such file or directory
It is required for saving/loading search history or cursor positions.

bandit31@bandit:/tmp/tmp.lmx9akaUcD/repo$ git add -f key.txt
bandit31@bandit:/tmp/tmp.lmx9akaUcD/repo$ git commit -m "Creando llave"
[master aa7873b] Creando llave
 1 file changed, 1 insertion(+)
 create mode 100644 key.txt
bandit31@bandit:/tmp/tmp.lmx9akaUcD/repo$ git push
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit31/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit31/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit31-git@localhost's password: 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 325 bytes | 325.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote: ### Attempting to validate files... ####
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
remote: Well done! Here is the password for the next level:
remote: 3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K 
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
To ssh://localhost:2220/home/bandit31-git/repo
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'ssh://localhost:2220/home/bandit31-git/repo'
```

## Notas Adicionales


## Referencias