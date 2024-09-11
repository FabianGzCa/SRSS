## Objetivo
I accidentally wrote the flag down. Good thing I deleted it! You download the challenge files here: [Archivo](https://artifacts.picoctf.net/c_titan/138/challenge.zip)

## Solución
```bash
wget https://artifacts.picoctf.net/c_titan/138/challenge.zip
unzip challenge.zip
cd drop-in
ls -la

git reflog
git chechout b562f0b
cat message.txt

picoCTF{s@n1t1z3_c785c319}

```

## Notas Adicionales


## Referencias
