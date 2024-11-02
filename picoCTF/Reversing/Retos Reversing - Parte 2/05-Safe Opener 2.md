## Objetivo
What can you do with this file?I forgot the key to my safe but this [file](https://artifacts.picoctf.net/c/290/SafeOpener.class) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?

## Solución
Le tiramos un strings al archivo y trae la flag:
```bash
strings SafeOpener.class 
<init>
Code
LineNumberTable
LocalVariableTable
this
LSafeOpener;
main
([Ljava/lang/String;)V
isOpen
args
[Ljava/lang/String;
keyboard
Ljava/io/BufferedReader;
encoder
Encoder
InnerClasses
Ljava/util/Base64$Encoder;
encodedkey
Ljava/lang/String;
StackMapTable
Exceptions
openSafe
(Ljava/lang/String;)Z
password
SourceFile
SafeOpener.java
java/io/BufferedReader
java/io/InputStreamReader
Enter password for the safe: 
java/lang/StringBuilder
You have  
 attempt(s) left
,picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_7db9fb8c}
```
picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_7db9fb8c}
## Notas Adicionales


## Referencias
