## Objetivo
Deberemos clonar el repositorio Git ubicado en `ssh://bandit29-git@localhost/home/bandit29-git/repo` usando el puerto 2220. La contraseña para el usuario `bandit29-git` es la misma que para el usuario `bandit29`. Luego de clonar el repositorio, investigaremos su contenido para encontrar la contraseña que nos permitirá avanzar al siguiente nivel.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit29
- **contraseña:** 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7

## Solución
```bash
bandit29@bandit:~$ mktemp -d
/tmp/tmp.gO1PREaupf
bandit29@bandit:~$ cd /tmp/tmp.gO1PREaupf
bandit29@bandit:/tmp/tmp.gO1PREaupf$ ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
-bash: ssh://bandit29-git@localhost:2220/home/bandit29-git/repo: No such file or directory
bandit29@bandit:/tmp/tmp.gO1PREaupf$ git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit29/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit29/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit29-git@localhost's password: 
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 16 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (16/16), done.
Resolving deltas: 100% (2/2), done.
bandit29@bandit:/tmp/tmp.gO1PREaupf$ cd repo/
bandit29@bandit:/tmp/tmp.gO1PREaupf/repo$ ls
README.md
bandit29@bandit:/tmp/tmp.gO1PREaupf/repo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>

bandit29@bandit:/tmp/tmp.gO1PREaupf/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
bandit29@bandit:/tmp/tmp.gO1PREaupf/repo$ git chechout dev
git: 'chechout' is not a git command. See 'git --help'.

The most similar command is
	checkout
bandit29@bandit:/tmp/tmp.gO1PREaupf/repo$ git checkout dev
branch 'dev' set up to track 'origin/dev'.
Switched to a new branch 'dev'
bandit29@bandit:/tmp/tmp.gO1PREaupf/repo$ ls
code  README.md
bandit29@bandit:/tmp/tmp.gO1PREaupf/repo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL
```

## Notas Adicionales


## Referencias