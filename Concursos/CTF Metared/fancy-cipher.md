## Objetivo
Reto Crypto
## Solución
Resuelto por: Externo: Peche

```
En este reto proporcionaban una serie de caracteres y numeros que al pareecer estaban encriptados, para desencriptarlo se uso un script:
```

```
enc = '-3(.4?B,5*9@7;065&0:&:6&-(5*@D'

def decode(data):
    dec = ''
    for shift in range(0, 0xff):
        for _ in data:
            dec += chr((ord(_)-shift) % 0xff)
        if 'flagmx' in dec:
            print('Decrypted flag: ', dec)
            return
    print('Couldn\'t find flag')

decode(enc)
```

```
Dando como salida la flag
```

```
flagmx{encryption_is_so_fancy}
```
## Notas adicionales
## Referencias