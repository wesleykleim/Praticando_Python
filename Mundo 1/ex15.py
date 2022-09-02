from math import trunc
num = float(input('Digite um número real: '))

print('O número digitado foi {} e sua porção inteira é {} '.format(num, trunc(num)))

print('-'*50)


num = float(input('Digite um número real: '))
print('O número digitado foi {} e sua porção inteira é {} '.format(num, int(num)))