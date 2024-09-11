## Objetivo
Run the Python script and convert the given number from decimal to binary to get the flag.
[script](https://artifacts.picoctf.net/c/24/convertme.py)

## Solución
```bash
wget https://artifacts.picoctf.net/c/24/convertme.py
echo "obase=2; ibase=10; 31" | bc
python3 convertme.py
picoCTF{4ll_y0ur_b4535_722f6b39}
```

## Notas Adicionales


## Referencias
