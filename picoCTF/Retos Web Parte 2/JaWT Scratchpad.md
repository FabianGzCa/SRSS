## Objetivo
Check the admin scratchpad! `https://jupiter.challenges.picoctf.org/problem/58210/` or http://jupiter.challenges.picoctf.org:58210

## Solución
En la página web tenemos un registro con solamente un nombre de usuario, intentamos admin y dice que no nos deja porque es un usuario especial, intentamos con cualquier otro y si nos deja pero no nos arroja notas guardadas, revisando las cookies vemos que hay una nueva llamada jwt por lo que podemos intuír que son las cookies de sesión, vamos a jwt.io para ver si podemos descifrar esta cookie y efectivamente contiene nuestro usuario, guardaremos el hash inicial en un archivo para buscar la contraseña, utilizamos el comando `hashcat archivoConHash /usr/share/wordlists/rockyou.txt` y nos retorna `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYSJ9.Wpx3_bxlH3-Q8LDfbdaCP3ML7bAdosK4mAHRXhDmhug:ilovepico` obteniendo la contraseña "ilovepico" ahora solo la sustituímos en jwt junto con el usuario que deseamos, en este caso admin y copiamos el hash generado `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.gtqDl4jVDvNbEe_JYEZTN19Vx6X9NNZtRVbKPBkhO-s` ahora lo sustituímos en la cookie de sesión que teníamos y recargamos, pudiendo ver las notas que había:

picoCTF{jawt_was_just_what_you_thought_44c752f5}




## Notas Adicionales


## Referencias
https://jwt.io