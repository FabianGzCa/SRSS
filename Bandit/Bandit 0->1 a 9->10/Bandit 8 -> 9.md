## Objetivo
Encontrar la contraseña en el archivo `data.txt`, identificando la única línea de texto que aparece solo una vez.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit2
- **contraseña:** dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

## Solución
```bash
ls -l
```
```text
total 20
-rw-r----- 1 bandit10 bandit9 19379 Jul 17 15:57 data.txt
```
```bash
sort data.txt | uniq -u
```
```text
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
```

## Notas Adicionales
#### Comandos:
* **sort {datos}**:  Ordena el archivo que le pasamos en {datos}.
* **uniq -u {archivo}**: detecta todos aquellas lineas duplicadas que están consecutivas y las ignora, mostrando solo aquellas que no son consecutivas en el archivo `{archivo}`
* **comando1 | comando2**: Toma el resultado de comando1 y lo pasa al comando2 

## Referencias