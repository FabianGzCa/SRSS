## Objetivo
Encontrar la contraseña en el archivo `data.txt` que está situada junto a la palabra `millionth`.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit7
- **contraseña:** morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

## Solución
```bash
ls -l
```
```text
-rw-r----- 1 bandit8 bandit7 4184396 Jul 17 15:57 data.txt
```
```bash
grep millionth data.txt
```
```text
millionth	dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
```

## Notas Adicionales
#### Comandos:
* **grep {busqueda} {archivo}**:  Busca el patrón especificado por `{busqueda}` dentro del archivo `{archivo}` y muestra las líneas que contienen ese patrón.

## Referencias