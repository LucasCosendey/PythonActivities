largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura*altura
print('Sua parede tem dimensao de {}x{} e sua área é de {:.2f}m².'.format(largura, altura, area))
tinta = area /2
print('Para pintar ela toda você vai precisar de {}l de tinta'.format(tinta))

