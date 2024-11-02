## Objetivo
You will find the flag after analysing this apkDownload [here](https://artifacts.picoctf.net/c/449/timer.apk).

## Solución
Obtenemos un .apk, lo descomprimimos:
unzip timer.apk
luego en los archivos que dejo buscamos el formato pico:
grep -r "pico"
nos da
grep: classes3.dex: binary file matches
entonces en classes3 buscamos de nuevo
strings classes3.dex | grep "pico"
dandonos la flag:
picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}

## Notas Adicionales


## Referencias
