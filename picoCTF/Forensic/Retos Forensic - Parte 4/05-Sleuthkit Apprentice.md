## Objetivo
Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/136/disk.flag.img.gz)

## Solución
Descomprimimos con `gunzip disk.flag.img.gz` dandonos el archivo disk.flag.img
Ahora utilizamos
```bash
sudo kpartx -v -a disk.flag.img
```
y nos da
`add map loop0p3 (254:2): 0 407552 linear 7:0 411648`
Utilizamos `mkdir Sleuthkit_Apprentice`
luego
`sudo mount /dev/mapper/loop1p3 Sleuthkit_Apprentice`
`cd mnt/root`
`catn flag.uni.txt`
picoCTF{by73_5urf3r_3497ae6b}


## Notas Adicionales


## Referencias
