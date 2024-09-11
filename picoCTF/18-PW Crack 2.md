## Objetivo
Can you crack the password to get the flag? Download the password checker [here](https://artifacts.picoctf.net/c/13/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/13/level2.flag.txt.enc) in the same directory too.


## Solución
```bash
wget https://artifacts.picoctf.net/c/13/level2.py
wget https://artifacts.picoctf.net/c/13/level2.flag.txt.enc
ls
nano level2.py
def level_2_pw_check():
    user_pw = (chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36))
    if( user_pw ==..............

python3 level2.py
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_489dea9a}
```

## Notas Adicionales


## Referencias
