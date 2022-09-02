#Crie um progrma que leia o nome completo de umapessoa e mostre:
#O nome com todas as letras maiúsculas e maiúsculas .
#quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: '))
print('Analisando seu nome: ...')
print('Seu nome em maíusculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}' .format(nome.lower()))
print('Seu nome tem {} letras '.format(len(nome)))

print('-'*30)
print('\n')



n = str(input('Digite seu nome completo ')).strip()#str deve estar presente como um cadeia de caracteres, sendo uma string cortada, elimando os espaços antes e depois das palavras.
print('Seu nome em maíusculo é {}'.format(n.upper()))
print('seu nome em minúsculo é {}'.format(n.lower()))
print('Seu nome tem um total de {} letras, sem os espaços.'.format(len(n) - n.count(' ')))#Metododo count está contando os espaços entre as palavras e subitraindo-as.


#Formas de ver quantas letras tem no primeiro nome
#Pesquisa dentro no nome encontre o primeiro espaço 
#metodo fid pesquisa onde está o primeiro wspaço, sendo que a posição 0 está na primeira letra e conta até o espaço.
print('Seu primeiro nome tem {} letras'.format(n.find(' ')))
#Split joga em uma lista os nomes inteiros 
separa = n.split()
print(separa)
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


