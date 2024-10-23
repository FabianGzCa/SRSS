## Objetivo
We found this weird message being passed around on the servers, we think we have a working decryption scheme. Download the message [here](https://artifacts.picoctf.net/c/129/message.txt). Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

## Solución
Nos dan el siguiente mensaje:
`350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213 `

Utilizando el archivo de mensaje que nos da, ejecutamos el siguiente archivo de python:
```python
def decode(number):
    r = number % 37
    return r

def main():
    f = open("message.txt", "r", encoding="UTF-8")
    lst = f.read().split()
    # print(lst[0])

    dec_lst = []

    for i in range(len(lst)):
        dec_lst.append(decode(int(lst[i])))

    abc="abcdefghijklmnopqrstuvwxyz0123456789_"
    print(len(abc))
    print(dec_lst)
    for letter in dec_lst:
        print(abc[letter],end="")

if __name__ == '__main__':
    main()
```
Y nos da lo siguiente:
r0und_n_r0und_add17ec2
le colocamos el formato de la flag:
picoCTF{r0und_n_r0und_add17ec2}
y esa será la flag 
## Notas Adicionales


## Referencias
