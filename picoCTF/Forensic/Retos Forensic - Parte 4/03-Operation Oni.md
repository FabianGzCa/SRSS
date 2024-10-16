## Objetivo
Download this disk image, find the key and log into the remote machine. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download disk image](https://artifacts.picoctf.net/c/69/disk.img.gz)
- Remote machine: `ssh -i key_file -p 57437 ctf-player@saturn.picoctf.net`

## Solución
Nos intentamos conectar con el comando que da y sale esto:
ssh -i key_file -p 57437 ctf-player@saturn.picoctf.net
Warning: Identity file key_file not accessible: No such file or directory.
Así que primero revisaremos el archivo:

gunzip disk.img.gz
dejandonos un disk.img

ahora utilizamos:
```bash
sudo kpartx -a -v disk.img 
```
que nos da
add map loop0p1 (254:0): 0 204800 linear 7:0 2048
add map loop0p2 (254:1): 0 264192 linear 7:0 206848
y ahora utilizamos
```bash
mkdir Operation_Oni
sudo mount /dev/mapper/loop0p2 Operation_Oni/
```
luego
`cd Operation_Oni/`
ahora
`sudo chmod 777 root`
para que nos deje entrar a root
`cd root/`
y con `ls -a` vemos que existe un .ssh, entramos con `sudo chmod 777 .ssh; cd .ssh` y ahí tenemos el id_ed25519 para conectarnos, le damos permiso 600 con `sudo chmod 600 id_ed25519` y entramos con el comando que nos dan `ssh -i id_ed25519 -p 59315 ctf-player@saturn.picoctf.net`

y entramos, con el comando `ls` notamos que hay un archivo flag.txt le tiramos `cat flag.txt` y nos da la flag
picoCTF{k3y_5l3u7h_339601ed}







## Notas Adicionales


## Referencias
