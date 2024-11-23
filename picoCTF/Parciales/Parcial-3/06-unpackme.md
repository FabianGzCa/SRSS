## Objetivo
Can you get the flag?Reverse engineer this [binary](https://artifacts.picoctf.net/c/204/unpackme-upx).

## Solución
Revisamos las propiedades del archivo:
```bash
❯ file unpackme-upx
unpackme-upx: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, no section header
```
lo descomprimimos:
```bash
upx -d unpackme-upx
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2024
UPX 4.2.2       Markus Oberhumer, Laszlo Molnar & John Reiser    Jan 3rd 2024

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
upx: unpackme-upx: NotPackedException: not packed by UPX

Unpacked 0 files.
❯ file unpackme-upx
unpackme-upx: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, BuildID[sha1]=5e4be04529afcdb8fa8855e3138c3f51047fa123, for GNU/Linux 3.2.0, not stripped
```

Abrimos el binario resultante con ghidra y analizamos el main:
```cpp
undefined8 main(void)

{
  long in_FS_OFFSET;
  int iStack_44;
  undefined8 uStack_40;
  undefined8 uStack_38;
  undefined8 uStack_30;
  undefined8 uStack_28;
  undefined4 uStack_20;
  undefined2 uStack_1c;
  long lStack_10;
  
  lStack_10 = *(long *)(in_FS_OFFSET + 0x28);
  uStack_38 = 0x4c75257240343a41;
  uStack_30 = 0x30623e306b6d4146;
  uStack_28 = 0x6865666430486637;
  uStack_20 = 0x36636433;
  uStack_1c = 0x4e;
  printf(&UNK_004b3004);
  __isoc99_scanf(&UNK_004b3020,&iStack_44);
  if (iStack_44 == 0xb83cb) {
    uStack_40 = rotate_encrypt(0,&uStack_38);
    fputs(uStack_40,stdout);
    putchar(10);
    free(uStack_40);
  }
  else {
    puts(&UNK_004b3023);
  }
  if (lStack_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```
Deberemos ejecutar el programa y pasarle el valor 754635
```bash
❯ chmod +x unpackme-upx
❯ ./unpackme-upx
What's my favorite number? 754635
picoCTF{up><_m3_f7w_e510a27f}
```
resultando en la flag

## Notas Adicionales


## Referencias
