## Objetivo
Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm) has extraordinarily helpful information...

## Solución
```bash
wget https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm
ls
chmod +x warm
❯ ./warm
Hello user! Pass me a -h to learn what I can do!
❯ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_616f7182}
```

## Notas Adicionales


## Referencias
