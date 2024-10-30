## Objetivo
Fix the syntax error in this Python script to print the flag.
[script](https://artifacts.picoctf.net/c/26/fixme1.py)

## Solución
```bash
wget https://artifacts.picoctf.net/c/26/fixme1.py
nano fixme1.py

flag = str_xor(flag_enc, 'enkidu')
print('That is correct! Here\'s your flag: ' + flag)

python3 fixme1.py

picoCTF{1nd3nt1ty_cr1515_09ee727a}
```

## Notas Adicionales


## Referencias
