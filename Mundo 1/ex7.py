n1 = float(input('Gigite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
soma = n1+n2+n3
media  = soma / 3

print('A primeira nota vale {} a segunda {} a terceira {} a soma das notas vale {} e a media aritimetica do aluno vale {:.2f} '.format(n1,n2,n3,soma,media))