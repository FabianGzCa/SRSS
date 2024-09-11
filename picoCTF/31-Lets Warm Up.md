## Objetivo
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

## Solución
```bash
echo "$(echo "obase=10; ibase=16; 70" | bc)" | awk '{ printf "%c\n", $1}'
p

picoCTF{p}
```

## Notas Adicionales


## Referencias
