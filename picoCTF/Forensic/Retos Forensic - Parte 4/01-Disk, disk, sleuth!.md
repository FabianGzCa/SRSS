## Objetivo
Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: [dds1-alpine.flag.img.gz](https://mercury.picoctf.net/static/ac394d24f88e51a09cc909687cf6d853/dds1-alpine.flag.img.gz)

## Solución
Descomprimimos el archivo
`gunzip dds1-alpine.flag.img.gz`

Buscamos con strings y grep un texto con el formato de la flag:
`strings dds1-alpine.flag.img | grep "picoCTF{"` y nos la da
SAY picoCTF{f0r3ns1c4t0r_n30phyt3_dcbf5942}

## Notas Adicionales


## Referencias
