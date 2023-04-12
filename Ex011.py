alt = float(input('Digite a altura da parede '))
larg = float(input('Digite a largura da parede '))
area = alt * larg

print('A altura da parede é {}, a largura da parede é {}, a área é {}m2'.format(alt, larg, area))

tinta = area / 2
print('A parede precisa de {}L de tinta'.format(tinta))