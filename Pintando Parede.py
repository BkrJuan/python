l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
tinta = area / 2

print('Sua Parede tem a dimensão de {}x{}, e sua area é de {}.'.format(l,a,area))
print('Para pintar sua parede, voce precisará de {} de tinta.'.format(tinta))