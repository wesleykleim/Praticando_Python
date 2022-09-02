import random
nome1 = input('Digite nome: ')
nome2 = input('Digite nome: ')
nome3 = input('Digite nome: ')
nome4 = input('Digite nome: ')

lista = [nome1,nome2,nome3,nome4]
escolhido = random.choice(lista)

print('O aluno escolhido foi {}'. format(escolhido))