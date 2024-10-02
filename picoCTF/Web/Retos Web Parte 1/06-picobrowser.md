## Objetivo
This website can be rendered only by **picobrowser**, go and catch the flag! `https://jupiter.challenges.picoctf.org/problem/50522/` ([link](https://jupiter.challenges.picoctf.org/problem/50522/)) or http://jupiter.challenges.picoctf.org:50522

## Solución
Nos dice que debemos entrar con el navegador picobrowser así que para engañarlo simplemente usamos curl -A "picobrowser" para definir que nuestro user-agent será picobrowser, además le damos un grep para que nos de la flag directamente
curl -A "picobrowser" https://jupiter.challenges.picoctf.org/problem/50522/flag | grep "pico"

```javascript
<p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{p1c0_s3cr3t_ag3nt_51414fa7}</code></p>
```


## Notas Adicionales


## Referencias
