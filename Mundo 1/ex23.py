n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(nome)
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}' .format(nome[len(nome)-1]))
#len de nome sabemos quantas posições tem nome, monstrando o nome na posição de len de nome  