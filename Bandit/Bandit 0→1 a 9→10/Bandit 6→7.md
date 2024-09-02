## Objetivo
Encontrar la contraseña almacenada en el servidor que sea propiedad del usuario `bandit7`, del grupo `bandit6`, y tenga un tamaño de 33 bytes.

## Datos de Acceso al Nivel
- **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit6
- **contraseña:** HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

## Solución
```bash
find / -user bandit7 -group bandit6 -size 33c 2> /dev/null
```
```text
/var/lib/dpkg/info/bandit7.password
```
```bash
cat /var/lib/dpkg/info/bandit7.password
```
```text
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
```
## Notas Adicionales
Dentro del comando `find`, `/` representa la raíz del sistema de archivos, por lo que buscará en todos los directorios y archivos del servidor. La opción `-user` especifica el usuario al que pertenece el objeto, y la opción `-group` indica el grupo al que pertenece. Con `2> /dev/null`, redirigimos los errores a `/dev/null` para que solo se muestren las salidas válidas.

## Referencias