real = float(input('Digite quanto você possu de dinheiro na carteira? R$'))
dolar = real / 5.18

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real,dolar))