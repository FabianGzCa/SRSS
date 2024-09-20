## Objetivo
The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? `https://jupiter.challenges.picoctf.org/problem/15796/` ([link](https://jupiter.challenges.picoctf.org/problem/15796/)) or http://jupiter.challenges.picoctf.org:15796

## Solución
entramos con cualquier usuario ( en este caso user: a password: a) y vemos que nos deja, revisamos las cookies y hay una llamada admin que contiene "False", la cambiamos a true y recargamos para que use esas cookies y listo tenemos la flag
`picoCTF{th3_c0nsp1r4cy_l1v3s_6edb3f5f}`

## Notas Adicionales


## Referencias
