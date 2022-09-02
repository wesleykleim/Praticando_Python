#Escreva um programa que faça o computador "Pensar " em um número inteiro entre 0 e 10 peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venseu ou perdeu.
from time import sleep
from random import randint
resp = 's'
computador = randint(0,10)
contJog = 0
contCop = 0
while resp == "s":
    print('-'*30)
    print('Vamos jogar...')
    jogador = int(input('Diga o número que pensei de 0 a 10: \n'))
    print('Processando...')
    sleep(3)

    if jogador == computador:
        print('Pensei no número {} você ganhou.'.format(computador))
        sleep(1)
        contJog = contJog + 1
        print('Está {}x{} pra você!'.format(contJog,contCop))
    else:
        print('Pensei em {} e não {} você perdeu!'.format(computador,jogador))
        sleep(1)
        contCop = contCop + 1
        print('Está {}x{} para o computador!'.format(contCop,contJog))

    resp = input('Deseja Continuar? (S/N)\n')

print('-'*30)
print('Quem será que venceu? ')
print('Calculando...')
sleep(6)
if contCop > contJog:
    print('Você perdeu para a minha IA de {} a {}, não foi dessa vez!'.format(contCop,contJog))
if contJog > contCop:
    print('Parabéns você conseguiu vencer da minha IA de {} a {}'.format(contJog,contCop))
if contJog == contCop:
    print('Que pena niguém ganhou, ficou no EMPATE!')
print('Acabou o jogo!')
