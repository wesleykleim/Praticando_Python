#Faça um número que leeia de 0 a 9999 e mostre na tela um código dos dígitos separados.
#Exemplo: número digitado 1234
num = int(input(' Informe um número: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print ('Analisando seu número {}'.format(num))
print('Unidade: {}'.format(unidade))
print('Dezena: {} '.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
