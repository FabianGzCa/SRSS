## Objetivo
Someone's commits seems to be preventing the program from working. Who is it? You can download the challenge files here: [Archivo](https://artifacts.picoctf.net/c_titan/156/challenge.zip)

## Solución
```bash
wget https://artifacts.picoctf.net/c_titan/156/challenge.zip

unzip challenge.zip
cd drop-in

ls -la

git log | grep "picoCTF{"
```

## Notas Adicionales


## Referencias
