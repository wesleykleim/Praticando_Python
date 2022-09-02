#Escreva um progra que pergunte a quantidade de km percorridos por um carro alugado e aquantidade de dias pelos quais foi alugado. Calcule o preço a pagar, sabendo queo carro custa R$ 60,00 por dias e R$ 0,15 por km rodado.



km = float(input('Digite a quantidade kilometros percorridos: '))
dias = int(input('Digite a quantidade de dias de aluguel '))
pagoDia = (dias * 60) + (km*0.15)
print('O total a pagar é {:.2f}'.format(pagoDia))

