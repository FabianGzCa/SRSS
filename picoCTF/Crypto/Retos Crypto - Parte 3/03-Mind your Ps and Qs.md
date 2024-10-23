## Objetivo
In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/3cfeb09681369c26e3f19d886bc1e5d9/values)

## Solución
Nos dan los siguientes valores
```bash
Decrypt my super sick RSA:
c: 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n: 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e: 65537
```
en
http://factordb.com
colocamos la n
Nos da
1617549722683965197900599011412144490161
y
475693130177488446807040098678772442581573

Instalamos una librería para cripto `pip install pycryptodome --break-system-packages`
Ejecutamos el siguiente código utilizando los valores que obtuvimos:
```python
from Crypto.Util.number import inverse, long_to_bytes

c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n = 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e = 65537
p = 1617549722683965197900599011412144490161
q = 475693130177488446807040098678772442581573

phi = (p-1)*(q-1)

d = inverse(e, phi)

m = pow(c,d,n)

print(long_to_bytes(m))
```
y nos da la flag al ejecutarlo:
picoCTF{sma11_N_n0_g0od_45369387}
## Notas Adicionales


## Referencias
