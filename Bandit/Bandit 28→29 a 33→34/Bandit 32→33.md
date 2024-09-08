## Objetivo
En este nivel, el desafío consiste en escapar del entorno limitado o del shell restringido al que te encuentras expuesto. Este tipo de desafío requiere que encuentres una manera de ejecutar comandos fuera de las restricciones impuestas por el entorno.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit32
- **contraseña:** 3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K

## Solución
```bash
WELCOME TO THE UPPERCASE SHELL
>> $0
$ bash
bandit33@bandit:~$ pwd              
/home/bandit32
bandit33@bandit:~$ cd /home/bandit33
bandit33@bandit:/home/bandit33$ ls -l 
total 4
-rw------- 1 bandit33 bandit33 430 Jul 17 15:57 README.txt
bandit33@bandit:/home/bandit33$ cat README.txt 
Congratulations on solving the last level of this game!

At this moment, there are no more levels to play in this game. However, we are constantly working
on new levels and will most likely expand this game with more levels soon.
Keep an eye out for an announcement on our usual communication channels!
In the meantime, you could play some of our other wargames.

If you have an idea for an awesome new level, please let us know!
```

## Notas Adicionales


## Referencias