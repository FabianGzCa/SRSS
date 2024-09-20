## Objetivo
Find the flag in the Python script! [Download Python script](https://artifacts.picoctf.net/c/37/serpentine.py)

## Solución
```bash
wget https://artifacts.picoctf.net/c/37/serpentine.py

nano serpentine.py

    elif choice == 'b':
      print_flag()
      print('\nOops! I must have misplaced the print_flag function! Check my source code!\n\n')

a) Print encouragement
b) Print flag
c) Quit

What would you like to do? (a/b/c) b
picoCTF{7h3_r04d_l355_7r4v3l3d_8e47d128}

```

## Notas Adicionales


## Referencias
