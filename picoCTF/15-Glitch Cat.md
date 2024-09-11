## Objetivo
Our flag printing service has started glitching!

## Solución
```bash
`nc saturn.picoctf.net 64345`

nano GC.py
print('picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}')

python3 GC.py
picoCTF{gl17ch_m3_n07_9c42a45d}
```

## Notas Adicionales


## Referencias
