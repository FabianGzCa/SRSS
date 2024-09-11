## Objetivo
Fix the syntax error in the Python script to print the flag.
[script](https://artifacts.picoctf.net/c/5/fixme2.py)

## Solución
```bash
wget https://artifacts.picoctf.net/c/5/fixme2.py
nano fixme2.py

  21   │ # Check that flag is not empty
  22   │ print('That is correct! Here\'s your flag: ' + flag)

python3 fixme2.py

picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}
```

## Notas Adicionales


## Referencias
