largura = float(input('Digite largura da parede:'))
alt = float(input('Altura da parede: '))
area = largura * alt

print('Sua parede tem dimensão de {}x{} e sua área é de {:.2f}m².'.format(largura,alt,area))
# A cada 2 metro² necessário 1L de tinta 

tinta = area / 2

print('Para pintar essa parede é necessário {:.2f} Litros de tinta '.format(tinta))