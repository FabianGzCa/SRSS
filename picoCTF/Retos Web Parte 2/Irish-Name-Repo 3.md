## Objetivo
There is a secure website running at `https://jupiter.challenges.picoctf.org/problem/40742/` ([link](https://jupiter.challenges.picoctf.org/problem/40742/)) or http://jupiter.challenges.picoctf.org:40742. Try to see if you can login as admin!

## Solución
Tenemos la url https://jupiter.challenges.picoctf.org/problem/40742/ en la que tenemos un menú de páginas que podemos visitar, hay un login de admin y si le damos nos redirige a https://jupiter.challenges.picoctf.org/problem/40742/login.html en el que al inspeccionar el código está esta línea:
```html
 <input type="hidden" name="debug" value="0">
```
cambiamos el value="0" por value="1" y al realizar una inyección sql básica 'or 1=1-- - nos arroja lo siguiente:
password: ' or 1=1-- -
SQL query: SELECT * FROM admin where password = '' be 1=1-- -'
donde notamos que si está lo que le pasamos `'' be 1=1-- -' ` pero en vez de or dice be, dandonos a entender que está cambiando el contenido que le pasamos, si pasamos abcdefghijklmnopqrstuvwxyz nos devuelve nopqrstuvwxyzabcdefghijklm, el mismo abecedario pero recorrido y si nos fijamos bien es un rot13, así que rotamos el or inicial 13 posiciones en el abecedario teniendo que mandarle la inyección rotada `'be 1=1-- -` y nos da la flag
picoCTF{3v3n_m0r3_SQL_4424e7af}

## Notas Adicionales


## Referencias
