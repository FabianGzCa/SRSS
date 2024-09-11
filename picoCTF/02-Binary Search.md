## Objetivo
Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses. Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools! You can download the challenge files here: [archivo](https://artifacts.picoctf.net/c_atlas/17/challenge.zip)

## Solución
Nos conectamos vía ssh al reto que se ejecutaba en la instancia y mediante busqueda binaria buscamos el número que nos pedia

```bash
ssh -p 57918 ctf-player@atlas.picoctf.net
myPassword
```
```text
Welcome to the Binary Search Game!
I'm thinking of a number between 1 and 1000.
Enter your guess: 500
Higher! Try again.
Enter your guess: 750
Lower! Try again.
Enter your guess: 625
Higher! Try again.
Enter your guess: 688
Higher! Try again.
Enter your guess: 719
Lower! Try again.
Enter your guess: 703
Lower! Try again.
Enter your guess: 695
Higher! Try again.
Enter your guess: 699
Higher! Try again.
Enter your guess: 701
Congratulations! You guessed the correct number: 701
Here's your flag: picoCTF{g00d_gu355_6dcfb67c}
Connection to atlas.picoctf.net closed.
```

## Notas Adicionales


## Referencias
