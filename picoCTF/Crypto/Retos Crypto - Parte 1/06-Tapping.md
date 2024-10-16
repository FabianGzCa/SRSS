## Objetivo
Theres tapping coming in from the wires. What's it saying `nc jupiter.challenges.picoctf.org 9422`.

## Solución
usamos el comando `nc jupiter.challenges.picoctf.org 9422`
y nos da `.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ..--- -.... ---.. ...-- ---.. ..--- ....- -.... .---- ----- } ` que al ser puntos y rayas sabemos que es código morse, lo pasamos a cyberchef y nos da lo siguiente:
PICOCTF{M0RS3C0D31SFUN2683824610}
que es la flag
## Notas Adicionales


## Referencias
https://gchq.github.io/CyberChef/#recipe=From_Morse_Code('Space','Line%20feed')&input=Li0tLiAuLiAtLi0uIC0tLSAtLi0uIC0gLi4tLiAtLSAtLS0tLSAuLS4gLi4uIC4uLi0tIC0uLS4gLS0tLS0gLS4uIC4uLi0tIC4tLS0tIC4uLiAuLi0uIC4uLSAtLiAuLi0tLSAtLi4uLiAtLS0uLiAuLi4tLSAtLS0uLiAuLi0tLSAuLi4uLSAtLi4uLiAuLS0tLSAtLS0tLQ