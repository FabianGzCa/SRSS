## Objetivo
How about we take you on an adventure on exploring certificate signing requests Take a look at this CSR file [here](https://artifacts.picoctf.net/c/426/readmycert.csr).

## Solución
```bash
catn readmycert.csr
-----BEGIN CERTIFICATE REQUEST-----
MIICpzCCAY8CAQAwPDEmMCQGA1UEAwwdcGljb0NURntyZWFkX215Y2VydF80MWQx
Yzc0Y30xEjAQBgNVBCkMCWN0ZlBsYXllcjCCASIwDQYJKoZIhvcNAQEBBQADggEP
ADCCAQoCggEBAOdcDj2/m1LxBrXb3ch9+2BtKd3b8NFn4USXA5JORPfeGcDdIX4V
SiRkFrbxLOit6SZwoAyWQ7SmWJTtzADbr82qTbVktGJj9YebwK57jpMEL6BPT9YA
cE9AGFtVJycL+IXqtlTqAGq4DjcPtAs5THgIPDJ+aTgRDHP8YItfEFs+aywLd8kS
WSmttEjS874Tc++b9PbQ246IIrtQ701/I1NB0S/inzQvPCui+hLSHgMFkGS4leN7
7xJORGAQueRejKuYnOs6HbAlbK0oIWKR83BxkntDBee8KhOPDynHDgYoblERl8rL
JAfcVogKNSniIztMkzh408V9mbLHOfsr6eUCAwEAAaAmMCQGCSqGSIb3DQEJDjEX
MBUwEwYDVR0lBAwwCgYIKwYBBQUHAwIwDQYJKoZIhvcNAQELBQADggEBAFEyhXpa
nZz/ofFW/31ryCF3nyvNg9pOyIniu8kcpiteSaOkNm4YREBCRwj92X3Wy1MUi/7Z
urXwR1TcRTxLdPqeVBn4nsJclAgZqMKcT0ftz5fAM/Xg5whwBHEBb1qFVN+HGhPo
1TKfhXunICyrjNWvM+2fudM2RPsGb0sBsjLAe1/6OJK82LJBoHQ0GlCPDN1tncrl
lpzHACCFPv7LMVF9BSkZDCQNglU1NYDDelXZezfXLbio/a1RC2k4rs+jorVmFese
elZFzORDsCzlgD87NvBUMZWI8J5+9fZeaWAQQfhwEiZOVn8IcjLUxUraxt4rbI/h
0EUJJuCjGyTjRpQ=
-----END CERTIFICATE REQUEST-----
```
Decodificamos de base64 este certificado y nos da un texto donde esta la flag:
picoCTF{read_mycert_41d1c74c}

## Notas Adicionales


## Referencias
