n = 50
a = n * 2
b = n * 3
c = n ** (1/2)

print('O dobro de {} é {}. \nE o tripo de {} é {}. \nA raiz quadrada de {} é {:.2f}'.format(n,a,n,b,n,c))
print('\n')

num = int(input('Digite um número:'))
print('O dobro de {} é {} \nOtriplo de {} é {} \nA raiz quadrada de {} é {:.2f}'.format(num,(num*2),num,(num*3),num, pow(num,(1/2))))