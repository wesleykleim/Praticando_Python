preco = float(input('Digite o valor do produto: '))
porcentagem = int(input('Dite o valor de porcentagem: '))
novoPreco = preco - (preco * porcentagem / 100)
valorDesconto = preco*porcentagem/100

print('Então {} % do valor de R${} é R${:.2f} e desconto foi de R${:.2f}'.format(porcentagem,preco,novoPreco,valorDesconto))