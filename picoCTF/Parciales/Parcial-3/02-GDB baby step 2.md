## Objetivo
Can you figure out what is in the `eax` register at the end of the `main` function? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.Debug [this](https://artifacts.picoctf.net/c/520/debugger0_b).

## Solución
Le damos permisos de ejecución al archivo y lo abrimos el archivo con GDB para obtener los datos necesarios


```bash
❯ chmod +x debugger0_b
❯ gdb debugger0_b
GNU gdb (Ubuntu 15.0.50.20240403-0ubuntu1) 15.0.50.20240403-git
Copyright (C) 2024 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from debugger0_b...
(No debugging symbols found in debugger0_b)
(gdb) info functions
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x0000000000401020  _start
0x0000000000401050  _dl_relocate_static_pie
0x0000000000401060  deregister_tm_clones
0x0000000000401090  register_tm_clones
0x00000000004010d0  __do_global_dtors_aux
0x0000000000401100  frame_dummy
0x0000000000401106  main
0x0000000000401150  __libc_csu_init
0x00000000004011c0  __libc_csu_fini
0x00000000004011c8  _fini
(gdb) dissassembly main
Undefined command: "dissassembly".  Try "help".
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:	endbr64
   0x000000000040110a <+4>:	push   %rbp
   0x000000000040110b <+5>:	mov    %rsp,%rbp
   0x000000000040110e <+8>:	mov    %edi,-0x14(%rbp)
   0x0000000000401111 <+11>:	mov    %rsi,-0x20(%rbp)
   0x0000000000401115 <+15>:	movl   $0x1e0da,-0x4(%rbp)
   0x000000000040111c <+22>:	movl   $0x25f,-0xc(%rbp)
   0x0000000000401123 <+29>:	movl   $0x0,-0x8(%rbp)
   0x000000000040112a <+36>:	jmp    0x401136 <main+48>
   0x000000000040112c <+38>:	mov    -0x8(%rbp),%eax
   0x000000000040112f <+41>:	add    %eax,-0x4(%rbp)
   0x0000000000401132 <+44>:	addl   $0x1,-0x8(%rbp)
   0x0000000000401136 <+48>:	mov    -0x8(%rbp),%eax
   0x0000000000401139 <+51>:	cmp    -0xc(%rbp),%eax
   0x000000000040113c <+54>:	jl     0x40112c <main+38>
   0x000000000040113e <+56>:	mov    -0x4(%rbp),%eax
   0x0000000000401141 <+59>:	pop    %rbp
   0x0000000000401142 <+60>:	ret
End of assembler dump.
(gdb) break main
Breakpoint 1 at 0x40110e
(gdb) run
Starting program: /home/fabiangzca/Documents/Escuela/SRSS/picoCTF/Parciales/Parcial-3/Reversing Parte 2/Archivos/debugger0_b 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x000000000040110e in main ()
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:	endbr64
   0x000000000040110a <+4>:	push   %rbp
   0x000000000040110b <+5>:	mov    %rsp,%rbp
=> 0x000000000040110e <+8>:	mov    %edi,-0x14(%rbp)
   0x0000000000401111 <+11>:	mov    %rsi,-0x20(%rbp)
   0x0000000000401115 <+15>:	movl   $0x1e0da,-0x4(%rbp)
   0x000000000040111c <+22>:	movl   $0x25f,-0xc(%rbp)
   0x0000000000401123 <+29>:	movl   $0x0,-0x8(%rbp)
   0x000000000040112a <+36>:	jmp    0x401136 <main+48>
   0x000000000040112c <+38>:	mov    -0x8(%rbp),%eax
   0x000000000040112f <+41>:	add    %eax,-0x4(%rbp)
   0x0000000000401132 <+44>:	addl   $0x1,-0x8(%rbp)
   0x0000000000401136 <+48>:	mov    -0x8(%rbp),%eax
   0x0000000000401139 <+51>:	cmp    -0xc(%rbp),%eax
   0x000000000040113c <+54>:	jl     0x40112c <main+38>
   0x000000000040113e <+56>:	mov    -0x4(%rbp),%eax
   0x0000000000401141 <+59>:	pop    %rbp
   0x0000000000401142 <+60>:	ret
End of assembler dump.
(gdb) break *(main+60)
Breakpoint 2 at 0x401142
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:	endbr64
   0x000000000040110a <+4>:	push   %rbp
   0x000000000040110b <+5>:	mov    %rsp,%rbp
=> 0x000000000040110e <+8>:	mov    %edi,-0x14(%rbp)
   0x0000000000401111 <+11>:	mov    %rsi,-0x20(%rbp)
   0x0000000000401115 <+15>:	movl   $0x1e0da,-0x4(%rbp)
   0x000000000040111c <+22>:	movl   $0x25f,-0xc(%rbp)
   0x0000000000401123 <+29>:	movl   $0x0,-0x8(%rbp)
   0x000000000040112a <+36>:	jmp    0x401136 <main+48>
   0x000000000040112c <+38>:	mov    -0x8(%rbp),%eax
   0x000000000040112f <+41>:	add    %eax,-0x4(%rbp)
   0x0000000000401132 <+44>:	addl   $0x1,-0x8(%rbp)
   0x0000000000401136 <+48>:	mov    -0x8(%rbp),%eax
   0x0000000000401139 <+51>:	cmp    -0xc(%rbp),%eax
   0x000000000040113c <+54>:	jl     0x40112c <main+38>
   0x000000000040113e <+56>:	mov    -0x4(%rbp),%eax
   0x0000000000401141 <+59>:	pop    %rbp
   0x0000000000401142 <+60>:	ret
End of assembler dump.
(gdb) info breakpoints
Num     Type           Disp Enb Address            What
1       breakpoint     keep y   0x000000000040110e <main+8>
	breakpoint already hit 1 time
2       breakpoint     keep y   0x0000000000401142 <main+60>
(gdb) continue
Continuing.

Breakpoint 2, 0x0000000000401142 in main ()
(gdb) info breakpoints
Num     Type           Disp Enb Address            What
1       breakpoint     keep y   0x000000000040110e <main+8>
	breakpoint already hit 1 time
2       breakpoint     keep y   0x0000000000401142 <main+60>
	breakpoint already hit 1 time
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:	endbr64
   0x000000000040110a <+4>:	push   %rbp
   0x000000000040110b <+5>:	mov    %rsp,%rbp
   0x000000000040110e <+8>:	mov    %edi,-0x14(%rbp)
   0x0000000000401111 <+11>:	mov    %rsi,-0x20(%rbp)
   0x0000000000401115 <+15>:	movl   $0x1e0da,-0x4(%rbp)
   0x000000000040111c <+22>:	movl   $0x25f,-0xc(%rbp)
   0x0000000000401123 <+29>:	movl   $0x0,-0x8(%rbp)
   0x000000000040112a <+36>:	jmp    0x401136 <main+48>
   0x000000000040112c <+38>:	mov    -0x8(%rbp),%eax
   0x000000000040112f <+41>:	add    %eax,-0x4(%rbp)
   0x0000000000401132 <+44>:	addl   $0x1,-0x8(%rbp)
   0x0000000000401136 <+48>:	mov    -0x8(%rbp),%eax
   0x0000000000401139 <+51>:	cmp    -0xc(%rbp),%eax
   0x000000000040113c <+54>:	jl     0x40112c <main+38>
   0x000000000040113e <+56>:	mov    -0x4(%rbp),%eax
   0x0000000000401141 <+59>:	pop    %rbp
=> 0x0000000000401142 <+60>:	ret
End of assembler dump.
(gdb) print $eax
$1 = 307019
```

obteniendo la flag:
picoCTF{307019}
## Notas Adicionales


## Referencias
