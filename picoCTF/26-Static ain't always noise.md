## Objetivo
Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/66932732825076cad4ba43e463dae82f/static)? This [BASH script](https://mercury.picoctf.net/static/66932732825076cad4ba43e463dae82f/ltdis.sh) might help!

## Solución
```bash
wget https://mercury.picoctf.net/static/66932732825076cad4ba43e463dae82f/static
strings static | grep "picoCTF{"
picoCTF{d15a5m_t34s3r_f5aeda17}
```

## Notas Adicionales


## Referencias
