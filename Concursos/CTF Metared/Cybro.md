## Objetivo
Hacer OSINT a un perfil de facebook
## Solución
Resuelto por: Fabian Martinez Alonso

```
En el reto nos proporcionaban un link de facebook para hacer Osint al perfil
```

```
Buscando por el perfil nos encontramos con un comentario en la foto de perfil de el bot o la persona
```

```
Guardamos esa info y seguimos investigando  
```

![Cybro](/imagenes/Cybro.jpg)

```
Viendo el perfil vemos que le gusta la pagina de Telegram asi que en base a eso buscamos su user en Telegram y vemos que si existe y le podemos mandar mensaje:
```

![Cybro 2](/imagenes/Cybro2.jpg)

```
Vemos que hay una opcion /challenge que nos da una flag encriptada
```

```
Deduciendo vemos que esta encriptada en Vignere asi que vamos a cyberchef y tratamos de desencriptarla pero neecesita una key, recordamos el comentario de facebook asi que tratamos con esso y vemos que si es, obtuvimos la flag
```

![Cybro 3](/imagenes/Cybro3.png)
## Notas adicionales
## Referencias