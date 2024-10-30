## Objetivo
Unzip this archive and find the file named 'uber-secret.txt' [Archivo](https://artifacts.picoctf.net/c/500/files.zip)

## Solución
```bash
wget https://artifacts.picoctf.net/c/500/files.zip
unzip files.zip
cd files
grep -r "picoCTF{"
picoCTF{f1nd_15_f457_ab443fd1}
```

## Notas Adicionales


## Referencias
