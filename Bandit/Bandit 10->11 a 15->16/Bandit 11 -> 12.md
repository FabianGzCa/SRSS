## Objetivo
Deberemos encontrar la contraseña en el archivo `data.txt`, donde todas las letras minúsculas y mayúsculas han sido rotadas 13 posiciones utilizando el cifrado ROT13. Para decodificar el texto y obtener la contraseña, se deberá usar el comando `tr`.

## Datos de Acceso al Nivel
 **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit2
- **contraseña:** dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

## Solución
```bash
ls -l
```
```text
total 4
-rw-r----- 1 bandit12 bandit11 49 Jul 17 15:57 data.txt
```
```bash
cat data.txt | tr [a-zA-Z] [n-za-mN-ZA-M]
```
```text
The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
```

## Notas Adicionales
Decodificamos el texto en el archivo `data.txt` que ha sido cifrado usando ROT13

## Referencias