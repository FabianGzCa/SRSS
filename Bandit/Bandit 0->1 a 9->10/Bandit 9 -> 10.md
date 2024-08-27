## Objetivo
Encontrar la contraseña en el archivo `data.txt`, que se encuentra en una de las pocas cadenas legibles por humanos precedidas por varios caracteres `=`.

## Datos de Acceso al Nivel
 **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit2
- **contraseña:** 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

## Solución
```bash
ls -l 
```
```text
total 20
-rw-r----- 1 bandit10 bandit9 19379 Jul 17 15:57 data.txt
```
```bash
strings data.txt | grep "==" | sed "s/.*==\s*//" | awk "length == 32"
```
```text
FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
```

## Notas Adicionales
#### Comandos:
* **strings {archivo}**:  captura secuencias de texto que tienen al menos 4 caracteres de longitud.
* **grep "\=\=" :** Busca las lineas que contengan `==` en la salida dada por el comando anterior.
* **sed "s/.*\=\=\s*\/\/":** **sed** es una herramienta de edición de texto en flujo. En el caso de la expresión que está como argumento, **sed** elimina cualquier texto que tenga `==`, incluyendo el contenido antes de estos, y en caso de haber espacios en blanco después, también los elimina (contando tanto espacios como tabulaciones).
* **awk "length == 32":** Filtra las líneas resultantes para mostrar solo aquellas que tienen exactamente los 32 caracteres mostrados en length.

## Referencias