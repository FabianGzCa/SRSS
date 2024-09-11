## Objetivo
How well can you perfom basic binary operations?

## Solución
```bash

Welcome to the Binary Challenge!"
Your task is to perform the unique operations in the given order and find the final result in hexadecimal that yields the flag.

Binary Number 1: 00110001
Binary Number 2: 01000001


Question 1/6:
Operation 1: '<<'
Perform a left shift of Binary Number 1 by 1 bits.

echo "obase=2; ibase=10; $(("0b00110001 << 0b1"))" | bc

Question 2/6:
Operation 2: '&'
Perform the operation on Binary Number 1&2.

echo "obase=2; ibase=10; $(("0b00110001 & 0b01000001"))" | bc

Question 3/6:
Operation 3: '*'
Perform the operation on Binary Number 1&2.

echo "obase=2; ibase=10; $(echo "obase=10; ibase=2; 00110001 * 01000001" | bc) " | bc

Question 4/6:
Operation 4: '>>'
Perform a right shift of Binary Number 2 by 1 bits .

echo "obase=2; ibase=10; $(("0b01000001 >> 0b1"))" | bc

Question 5/6:
Operation 5: '+'
Perform the operation on Binary Number 1&2.

echo "obase=2; ibase=10; $(echo "obase=10; ibase=2; 00110001 + 01000001" | bc) " | bc

Question 6/6:
Operation 6: '|'
Perform the operation on Binary Number 1&2.

echo "obase=2; ibase=10; $(("0b00110001 | 0b01000001"))" | bc

Enter the results of the last operation in hexadecimal

echo "obase=16; ibase=10; $(("0b00110001 | 0b01000001"))" | bc
```

## Notas Adicionales


## Referencias
