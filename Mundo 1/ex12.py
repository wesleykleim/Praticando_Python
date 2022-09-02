salario = float(input('Digite o sálario do funcionário: '))

porcentagem = int(input('Digite o valor de porcentagem para aumento: '))
novoSalario = salario + (salario * porcentagem / 100)
aumento = salario*porcentagem / 100

print('O salário do funcionário obeteve aumento de {}% \nSeu valor era de R${:.2f} e passou a R${:.2f} \nO aumento foi de R${:.2f}'.format(porcentagem,salario,novoSalario,aumento))