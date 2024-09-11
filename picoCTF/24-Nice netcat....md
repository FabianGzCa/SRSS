## Objetivo
There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 7449`, but it doesn't speak English...

## Solución
```bash
nc mercury.picoctf.net 7449 | awk '{for(i=1;i<=NF;i++) printf "%c", $i; printf ""}'
picoCTF{g00d_k1tty!_n1c3_k1tty!_f2d7cafa}
```

## Notas Adicionales
NF representa el número de líneas

## Referencias
