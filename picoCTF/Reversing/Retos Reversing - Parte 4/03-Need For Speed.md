## Objetivo
The name of the game is [speed](https://www.youtube.com/watch?v=8piqd2BWeGI). Are you quick enough to solve this problem and keep it above 50 mph? [need-for-speed](https://jupiter.challenges.picoctf.org/static/27dd5548b14661f65ce3ac6a8a8f575b/need-for-speed).

## Solución

Revisamos información básica del archivo:
```bash
❯ file need-for-speed
need-for-speed: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=2d0d401d07683664113690a7fb94413a0039d228, not stripped
❯ chmod +x need-for-speed
❯ ./need-for-speed
Keep this thing over 50 mph!
============================

Creating key...
Not fast enough. BOOM!

❯ objdump -D need-for-speed -M intel | grep '<main>' -A20
 67d:   48 8d 3d 96 02 00 00    lea    rdi,[rip+0x296]        # 91a <main>
 684:   ff 15 56 09 20 00       call   QWORD PTR [rip+0x200956]        # 200fe0 <__libc_start_main@GLIBC_2.2.5>
 68a:   f4                      hlt
 68b:   0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000000690 <deregister_tm_clones>:
 690:   48 8d 3d c1 09 20 00    lea    rdi,[rip+0x2009c1]        # 201058 <__TMC_END__>
 697:   55                      push   rbp
 698:   48 8d 05 b9 09 20 00    lea    rax,[rip+0x2009b9]        # 201058 <__TMC_END__>
 69f:   48 39 f8                cmp    rax,rdi
 6a2:   48 89 e5                mov    rbp,rsp
 6a5:   74 19                   je     6c0 <deregister_tm_clones+0x30>
 6a7:   48 8b 05 2a 09 20 00    mov    rax,QWORD PTR [rip+0x20092a]        # 200fd8 <_ITM_deregisterTMCloneTable>
 6ae:   48 85 c0                test   rax,rax
 6b1:   74 0d                   je     6c0 <deregister_tm_clones+0x30>
 6b3:   5d                      pop    rbp
 6b4:   ff e0                   jmp    rax
 6b6:   66 2e 0f 1f 84 00 00    cs nop WORD PTR [rax+rax*1+0x0]
 6bd:   00 00 00 
 6c0:   5d                      pop    rbp
 6c1:   c3                      ret
--
000000000000091a <main>:
 91a:   55                      push   rbp
 91b:   48 89 e5                mov    rbp,rsp
 91e:   48 83 ec 10             sub    rsp,0x10
 922:   89 7d fc                mov    DWORD PTR [rbp-0x4],edi
 925:   48 89 75 f0             mov    QWORD PTR [rbp-0x10],rsi
 929:   b8 00 00 00 00          mov    eax,0x0
 92e:   e8 a5 ff ff ff          call   8d8 <header>
 933:   b8 00 00 00 00          mov    eax,0x0
 938:   e8 f2 fe ff ff          call   82f <set_timer>
 93d:   b8 00 00 00 00          mov    eax,0x0
 942:   e8 36 ff ff ff          call   87d <get_key>
 947:   b8 00 00 00 00          mov    eax,0x0
 94c:   e8 5b ff ff ff          call   8ac <print_flag>
 951:   b8 00 00 00 00          mov    eax,0x0
 956:   c9                      leave
 957:   c3                      ret
 958:   0f 1f 84 00 00 00 00    nop    DWORD PTR [rax+rax*1+0x0]
 95f:   00 

0000000000000960 <__libc_csu_init>:

```
Nos ponemos a depurar con gdb:
```bash
❯ gdb need-for-speed
(gdb) set disassembly-flavor intel
(gdb) disassemble main
Dump of assembler code for function main:
   0x000000000000091a <+0>:       push   rbp
   0x000000000000091b <+1>:       mov    rbp,rsp
   0x000000000000091e <+4>:       sub    rsp,0x10
   0x0000000000000922 <+8>:       mov    DWORD PTR [rbp-0x4],edi
   0x0000000000000925 <+11>:      mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000000929 <+15>:      mov    eax,0x0
   0x000000000000092e <+20>:      call   0x8d8 <header>
   0x0000000000000933 <+25>:      mov    eax,0x0
   0x0000000000000938 <+30>:      call   0x82f <set_timer>
   0x000000000000093d <+35>:      mov    eax,0x0
   0x0000000000000942 <+40>:      call   0x87d <get_key>
   0x0000000000000947 <+45>:      mov    eax,0x0
   0x000000000000094c <+50>:      call   0x8ac <print_flag>
   0x0000000000000951 <+55>:      mov    eax,0x0
   0x0000000000000956 <+60>:      leave
   0x0000000000000957 <+61>:      ret
End of assembler dump.
(gdb) break main
Breakpoint 1 at 0x91e
(gdb) info breakpoints
Num     Type           Disp Enb Address            What
1       breakpoint     keep y   0x000000000000091e <main+4>
(gdb) run
Starting program: /home/fabiangzca/Documents/Escuela/SRSS/picoCTF/Reversing/Retos Reversing - Parte 4/Archivos/need-for-speed 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x000055555540091e in main ()
(gdb) disassemble main
Dump of assembler code for function main:
   0x000055555540091a <+0>:       push   rbp
   0x000055555540091b <+1>:       mov    rbp,rsp
=> 0x000055555540091e <+4>:       sub    rsp,0x10
   0x0000555555400922 <+8>:       mov    DWORD PTR [rbp-0x4],edi
   0x0000555555400925 <+11>:      mov    QWORD PTR [rbp-0x10],rsi
   0x0000555555400929 <+15>:      mov    eax,0x0
   0x000055555540092e <+20>:      call   0x5555554008d8 <header>
   0x0000555555400933 <+25>:      mov    eax,0x0
   0x0000555555400938 <+30>:      call   0x55555540082f <set_timer>
   0x000055555540093d <+35>:      mov    eax,0x0
   0x0000555555400942 <+40>:      call   0x55555540087d <get_key>
   0x0000555555400947 <+45>:      mov    eax,0x0
   0x000055555540094c <+50>:      call   0x5555554008ac <print_flag>
   0x0000555555400951 <+55>:      mov    eax,0x0
   0x0000555555400956 <+60>:      leave
   0x0000555555400957 <+61>:      ret
End of assembler dump.
(gdb) call (int) get_key()
Creating key...
Finished
$1 = 9
(gdb) call (int) print_flag()
Printing flag:
PICOCTF{Good job keeping bus #1f2ac4ec speeding along!}
$2 = 56
(gdb) PICOCTF{Good job keeping bus #1f2ac4ec speeding along!}
```
y nos da la flag:
`PICOCTF{Good job keeping bus #1f2ac4ec speeding along!}`

## Notas Adicionales


## Referencias
