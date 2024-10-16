## Objetivo
Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/214/disk.flag.img.gz)

## Solución
Descomprimimos con `gunzip disk.flag.img.gz` dandonos el archivo disk.flag.img
ahora utilizamos ```
sudo kpartx -a -v disk.flag.img```
nos da
`add map loop0p3 (254:2): 0 407552 linear 7:0 411648`
entonces utilizamos
`mkdir Operation_Orchid
y posteriormente
```
sudo mount /dev/mapper/loop0p3 Operation_Orchid
```
y usamos `sudo su ` para movernos con mayor comodidad
vamos a /root/ y  con el comando `ls -a` notamos un archivo flag.txt.enc, pero también un .ash_history, lo revisamos y vemos la siguiente línea interesante:
```
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
```
desencriptamos la flag con:
```
openssl aes256 -d --in flag.txt.enc -k unbreakablepassword1234567
```
y nos da la flag:
picoCTF{h4un71ng_p457_1d02081e}




## Notas Adicionales


## Referencias
