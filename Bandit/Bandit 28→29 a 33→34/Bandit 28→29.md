## Objetivo
Deberemos clonar el repositorio Git ubicado en `ssh://bandit28-git@localhost/home/bandit28-git/repo` utilizando el puerto 2220. La contraseña para el usuario `bandit28-git` es la misma que la de `bandit28`. Una vez clonado el repositorio, exploraremos su contenido para encontrar la contraseña para el siguiente nivel.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit28
- **contraseña:** Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN

## Solución
```bash
mktem -d
cd /tmp/tmp.DqgxmdYYqp/
git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
git log
commit 8cbd1e08d1879415541ba19ddee3579e80e3f61a (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Wed Jul 17 15:57:30 2024 +0000

    fix info leak

commit 73f5d0435070c8922da12177dc93f40b2285e22a
Author: Morla Porla <morla@overthewire.org>
Date:   Wed Jul 17 15:57:30 2024 +0000

    add missing data

commit 5f7265568c7b503b276ec20f677b68c92b43b712
Author: Ben Dover <noone@overthewire.org>
Date:   Wed Jul 17 15:57:30 2024 +0000

    initial commit of README.md

git show 8cbd1e08d1879415541ba19ddee3579e80e3f61a
commit 8cbd1e08d1879415541ba19ddee3579e80e3f61a (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Wed Jul 17 15:57:30 2024 +0000

    fix info leak

diff --git a/README.md b/README.md
index d4e3b74..5c6457b 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials
 
 - username: bandit29
-- password: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7
+- password: xxxxxxxxxx
 
```

## Notas Adicionales


## Referencias