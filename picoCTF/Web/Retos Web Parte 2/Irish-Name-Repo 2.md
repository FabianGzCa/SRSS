## Objetivo
There is a website running at `https://jupiter.challenges.picoctf.org/problem/53751/` ([link](https://jupiter.challenges.picoctf.org/problem/53751/)). Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login! or http://jupiter.challenges.picoctf.org:53751

## Solución
Tenemos la url https://jupiter.challenges.picoctf.org/problem/53751/ en la que tenemos un menú de páginas que podemos visitar, hay un login de admin y si le damos nos redirige a https://jupiter.challenges.picoctf.org/problem/53751/login.html donde intentamos una inyección sql básica con admin' and 1=1-- - de usuario y cualquier contraseña pudiendo loguearnos y  consiguiendo la flag.

picoCTF{m0R3_SQL_plz_c34df170}

## Notas Adicionales


## Referencias
