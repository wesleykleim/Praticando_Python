#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math
catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
'''
hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
print('A hipotenusa vai meditr {:.2f}'.format(hipotenusa))
'''
hipotenusa1 =math.hypot(catetoOposto,catetoAdjacente)
print('A hipotenusa vai meditr {:.2f}'.format(hipotenusa1))