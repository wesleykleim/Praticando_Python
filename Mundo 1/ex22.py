#Faça um progrma que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em qual posição ela aprece a primeira vez, e em que posição ela aparece a ultima vez


from itertools import count


frase= str(input('Digite uma frase: ')).upper().strip()

print('A letra A aprece {} vezes na frase '.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
