print('Aviso do professor quem chegar atrados mais de 3 vezes leva suspensão ')
numero_atraso = input('Chegou atrasado? ')

while True:
    quatsAtraso = int(input('Quantas vezes chegou atrasado '))

    if quatsAtraso > 3:
        print('Desculpe mas agora você vai receber uma suspensão')
    elif quatsAtraso == 3:
        print('Pela 3º vez você se atrasou, na próxima é suspensão ')
    elif quatsAtraso == 2:
        print('É a segunda vez que se atrasa, cuidado!')
    else:
        print('O que aconteceu, é a primeira vez em que se atrasa!')

