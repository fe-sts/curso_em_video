#Faça um programa que leia a largura ea altura de uma parede em metros, calcula a sua área e a quantidade de tinta necessaria para pintá-la sabendo que cada litro de tinta pinta uma área de 2m².

alt = float(input('Calcule quantos litros de tinta você precisa! (Digite em metros ex: 10.5)\nEntre com a altura da parede: '))
larg = float(input('Entre com a largura da parede: '))

#1 litro = 2m²
area = alt * larg
print(area)
print('Você precisa de {} litros de tinta para pintar a parede!'.format(area/2))

