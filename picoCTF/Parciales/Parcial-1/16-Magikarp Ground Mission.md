## Objetivo
Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `ee388b88`

## Solución
```bash
`ssh ctf-player@venus.picoctf.net -p 60606`

ls

cat 1of3.flag.txt 
picoCTF{xxsh_

cat instructions-to-2of3.txt
cd /

cat 2of3.flag.txt 
0ut_0f_\/\/4t3r_

cat instructions-to-3of3.txt
cd /home/ctf-player/
cat 3of3.flag.txt
3ca613a1}

picoCTF{xxsh_0ut_0f_\/\/4t3r_3ca613a1}
```

## Notas Adicionales


## Referencias
