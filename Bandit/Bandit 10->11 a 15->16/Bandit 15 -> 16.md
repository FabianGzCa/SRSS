## Objetivo
Deberemos recuperar la contraseña para el siguiente nivel enviando la contraseña del nivel actual al puerto 30001 en `localhost` utilizando cifrado SSL/TLS. Para esto, se puede usar el comando `openssl s_client` para establecer una conexión segura con el puerto especificado y enviar la contraseña. Si se obtienen respuestas como “DONE”, “RENEGOTIATING” o “KEYUPDATE”, se debe consultar la sección "CONNECTED COMMANDS" en la manpage para manejar estas situaciones.

## Datos de Acceso al Nivel
 **comando:** ssh
- **host:** bandit.labs.overthewire.org
- **puerto:** 2220
- **usuario:** bandit2
- **contraseña:** 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

## Solución
```bash
openssl s_client -connect localhost:30001
```
```text
openssl s_client -connect localhost:30001
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
---
Certificate chain
 0 s:CN = SnakeOil
   i:CN = SnakeOil
   a:PKEY: rsaEncryption, 4096 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 10 03:59:50 2024 GMT; NotAfter: Jun  8 03:59:50 2034 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFBzCCAu+gAwIBAgIUBLz7DBxA0IfojaL/WaJzE6Sbz7cwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIU25ha2VPaWwwHhcNMjQwNjEwMDM1OTUwWhcNMzQwNjA4
MDM1OTUwWjATMREwDwYDVQQDDAhTbmFrZU9pbDCCAiIwDQYJKoZIhvcNAQEBBQAD
ggIPADCCAgoCggIBANI+P5QXm9Bj21FIPsQqbqZRb5XmSZZJYaam7EIJ16Fxedf+
jXAv4d/FVqiEM4BuSNsNMeBMx2Gq0lAfN33h+RMTjRoMb8yBsZsC063MLfXCk4p+
09gtGP7BS6Iy5XdmfY/fPHvA3JDEScdlDDmd6Lsbdwhv93Q8M6POVO9sv4HuS4t/
jEjr+NhE+Bjr/wDbyg7GL71BP1WPZpQnRE4OzoSrt5+bZVLvODWUFwinB0fLaGRk
GmI0r5EUOUd7HpYyoIQbiNlePGfPpHRKnmdXTTEZEoxeWWAaM1VhPGqfrB/Pnca+
vAJX7iBOb3kHinmfVOScsG/YAUR94wSELeY+UlEWJaELVUntrJ5HeRDiTChiVQ++
wnnjNbepaW6shopybUF3XXfhIb4NvwLWpvoKFXVtcVjlOujF0snVvpE+MRT0wacy
tHtjZs7Ao7GYxDz6H8AdBLKJW67uQon37a4MI260ADFMS+2vEAbNSFP+f6ii5mrB
18cY64ZaF6oU8bjGK7BArDx56bRc3WFyuBIGWAFHEuB948BcshXY7baf5jjzPmgz
mq1zdRthQB31MOM2ii6vuTkheAvKfFf+llH4M9SnES4NSF2hj9NnHga9V08wfhYc
x0W6qu+S8HUdVF+V23yTvUNgz4Q+UoGs4sHSDEsIBFqNvInnpUmtNgcR2L5PAgMB
AAGjUzBRMB0GA1UdDgQWBBTPo8kfze4P9EgxNuyk7+xDGFtAYzAfBgNVHSMEGDAW
gBTPo8kfze4P9EgxNuyk7+xDGFtAYzAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3
DQEBCwUAA4ICAQAKHomtmcGqyiLnhziLe97Mq2+Sul5QgYVwfx/KYOXxv2T8ZmcR
Ae9XFhZT4jsAOUDK1OXx9aZgDGJHJLNEVTe9zWv1ONFfNxEBxQgP7hhmDBWdtj6d
taqEW/Jp06X+08BtnYK9NZsvDg2YRcvOHConeMjwvEL7tQK0m+GVyQfLYg6jnrhx
egH+abucTKxabFcWSE+Vk0uJYMqcbXvB4WNKz9vj4V5Hn7/DN4xIjFko+nREw6Oa
/AUFjNnO/FPjap+d68H1LdzMH3PSs+yjGid+6Zx9FCnt9qZydW13Miqg3nDnODXw
+Z682mQFjVlGPCA5ZOQbyMKY4tNazG2n8qy2famQT3+jF8Lb6a4NGbnpeWnLMkIu
jWLWIkA9MlbdNXuajiPNVyYIK9gdoBzbfaKwoOfSsLxEqlf8rio1GGcEV5Hlz5S2
txwI0xdW9MWeGWoiLbZSbRJH4TIBFFtoBG0LoEJi0C+UPwS8CDngJB4TyrZqEld3
rH87W+Et1t/Nepoc/Eoaux9PFp5VPXP+qwQGmhir/hv7OsgBhrkYuhkjxZ8+1uk7
tUWC/XM0mpLoxsq6vVl3AJaJe1ivdA9xLytsuG4iv02Juc593HXYR8yOpow0Eq2T
U5EyeuFg5RXYwAPi7ykw1PW7zAPL4MlonEVz+QXOSx6eyhimp1VZC11SCg==
-----END CERTIFICATE-----
subject=CN = SnakeOil
issuer=CN = SnakeOil
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2103 bytes and written 373 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 4096 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 30A78C205DDD3967F87459717CD0F1856E0562CFA34BB5AA15DAE68CAE240912
    Session-ID-ctx: 
    Resumption PSK: 409B862003FF0EDBCC5EE19F28F73EDA633CF744AE75E7699AFD35FB1A069140D6534C9B7F05C14278BBBD01D4A49E0F
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - 43 87 d0 c4 a5 49 95 26-c8 3e eb 08 d7 47 78 ca   C....I.&.>...Gx.
    0010 - 92 bd 14 59 cd ec 0a 00-3b 60 28 36 e6 96 b6 14   ...Y....;`(6....
    0020 - 9c 76 75 b2 a4 ef 9c 52-28 58 1a d7 70 3e 01 b2   .vu....R(X..p>..
    0030 - bc 09 bd 07 65 b8 6b 78-06 de df 03 c9 e7 15 98   ....e.kx........
    0040 - 2a 67 b3 44 00 9a fa 4d-ee 0f d0 7d df 4b 48 fa   *g.D...M...}.KH.
    0050 - 4e e6 85 67 19 2c 39 ef-76 99 85 35 08 fe b0 a3   N..g.,9.v..5....
    0060 - b8 aa d5 9e 04 f8 11 db-6c 92 c2 2c 46 33 7a 26   ........l..,F3z&
    0070 - bc c7 36 db 02 6f 37 34-e5 e5 d5 73 a0 7b 0b 1f   ..6..o74...s.{..
    0080 - 6b 83 fa 08 8d 75 79 5d-20 ef 93 cb ce 0b bf ab   k....uy] .......
    0090 - fd a1 b0 0f 43 4f fe d0-b3 49 93 a7 06 43 09 1d   ....CO...I...C..
    00a0 - 07 0e 0a ec 7b b1 8c eb-53 88 8e 53 41 f7 0a 88   ....{...S..SA...
    00b0 - 89 26 a7 94 6d 48 45 54-d2 d6 81 b2 e4 21 0e 9b   .&..mHET.....!..
    00c0 - 8d 26 4c 82 44 38 92 64-26 a9 fb d7 ea b4 53 b3   .&L.D8.d&.....S.
    00d0 - 98 1d 99 dd f5 c3 91 b8-e1 62 b8 69 2b 5b 44 8f   .........b.i+[D.

    Start Time: 1724998730
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 102C5958A118A7BFA041B84742A5FF76BEF215901426C97C12393D81861F1CAD
    Session-ID-ctx: 
    Resumption PSK: D2024398430FE320E91C42F5F2DDA91F7AF91FCDA25254D8A448511C4DB07359BD9C80FB91EF50A7A3C8C87ACCA7749C
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - 43 87 d0 c4 a5 49 95 26-c8 3e eb 08 d7 47 78 ca   C....I.&.>...Gx.
    0010 - 85 b2 74 cc d9 92 3f 46-f5 67 fa d2 d8 93 d7 38   ..t...?F.g.....8
    0020 - 4f 82 d7 82 48 90 5a 60-71 30 13 02 d0 54 17 a4   O...H.Z`q0...T..
    0030 - 7b 86 bf 8e fc f6 b9 54-aa c3 85 17 76 88 fe f2   {......T....v...
    0040 - 08 7a 32 17 a6 df e9 1f-8e 8d 9f 8f 12 2d 65 5a   .z2..........-eZ
    0050 - 5c b5 f4 12 7d 97 74 f7-54 99 f5 32 c9 94 9f 13   \...}.t.T..2....
    0060 - 5d 81 a5 03 d1 aa 5f cb-58 23 33 b6 4c d1 5d 8a   ]....._.X#3.L.].
    0070 - 11 75 d0 aa b3 cc e6 f8-95 e3 a1 ff a9 f7 1e 45   .u.............E
    0080 - b9 4f b8 d5 38 01 72 21-2c d1 74 22 a3 5e b4 1a   .O..8.r!,.t".^..
    0090 - b2 b6 8e 22 36 c7 ee 24-db ad bf b2 98 5b 21 9f   ..."6..$.....[!.
    00a0 - 7c 03 b8 12 94 c1 45 62-71 52 d2 ac d6 7d a7 5c   |.....EbqR...}.\
    00b0 - 36 01 74 20 10 1d db 47-1d dc d8 e6 92 39 02 17   6.t ...G.....9..
    00c0 - 41 25 b8 e0 d6 71 7a 4e-56 78 0f 68 c8 4c 3a 11   A%...qzNVx.h.L:.
    00d0 - 93 2b 37 54 7b 3c 20 ef-86 13 33 82 9d 9d 86 5c   .+7T{< ...3....\

    Start Time: 1724998730
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
Correct!
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx

closed
```

## Notas Adicionales
El comando `openssl s_client -connect localhost:30001` establece una conexión SSL/TLS al puerto 30001 en `localhost`, permitiendo la comunicación segura y la visualización de información sobre el certificado y la conexión cifrada.

## Referencias