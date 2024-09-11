## Objetivo
Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings) without running it?

## Solución
```bash
wget https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings

strings strings | grep "picoCTF{"
picoCTF{5tRIng5_1T_d66c7bb7}
```

## Notas Adicionales


## Referencias
