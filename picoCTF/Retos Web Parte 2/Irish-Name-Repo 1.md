## Objetivo
There is a website running at `https://jupiter.challenges.picoctf.org/problem/50009/` ([link](https://jupiter.challenges.picoctf.org/problem/50009/)) or http://jupiter.challenges.picoctf.org:50009. Do you think you can log us in? Try to see if you can login!

## Solución
Tenemos la url https://jupiter.challenges.picoctf.org/problem/50009/ en la que tenemos un menú de páginas que podemos visitar, hay un login de admin y si le damos nos redirige a https://jupiter.challenges.picoctf.org/problem/50009/login.html donde intentamos una inyección sql básica con admin' or 1=1-- - de usuario y cualquier contraseña pudiendo loguearnos y  consiguiendo la flag.

picoCTF{s0m3_SQL_fb3fe2ad}
## Notas Adicionales


## Referencias
