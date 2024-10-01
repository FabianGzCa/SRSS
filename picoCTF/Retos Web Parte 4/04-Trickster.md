## Objetivo
I found a web app that can help process images: PNG images only!

## Solución
La página solicita que subamos una imágen, intenté subiendo una webShell en php con los números magicos modificados para que parezca una PNG y además modifique la extensión a .png.php y revisando el /robots.txt podemos ir a /uploads donde se guardan las imagenes, voy a /uploads/webShell.png.php y funciona, ahora me mando una revese shell y tirandole el comando:
grep -r 'picoCTF' /var/www/html para buscar la flag ahi mediante la url:
http://atlas.picoctf.net:58420/uploads/webShellImage.png.php?c=grep%20-r%20%27picoCTF%27%20/var/www/html
nos devuelve:
`�PNG/var/www/html/HFQWKODGMIYTO.txt:/* picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_9ae8fb17} */`

lugar donde esta la flag:

picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_9ae8fb17}

## Notas Adicionales


## Referencias
