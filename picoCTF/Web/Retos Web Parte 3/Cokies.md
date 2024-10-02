## Objetivo
Who doesn't love cookies? Try to figure out the best one. [http://mercury.picoctf.net:54219/](http://mercury.picoctf.net:54219/)

## Solución
Entramos a la URL y vemos que si cambiamos la cookie para obtener un resultado diferente ya no nos deja utilizarla por lo que mejor utilizamos curl `curl --cookie "name=1" http://mercury.picoctf.net:54219/check` y al probar con el name 18 y ahí obtenemos la flag `picoCTF{3v3ry1_l0v3s_c00k135_96cdadfd}`

## Notas Adicionales
Lo mandamos a /check dado que al revisar las peticiones al mandar una cookie las está mandando a ahí 

## Referencias
