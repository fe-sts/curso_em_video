#Faça um programa que leia o comprimento da cateto Oposto e do Cateto Adjacente de um triângulo retângulo,
#calcule e mostre o comprimento da hipotenusa

cat_op = float(input('Entre com o valor do comprimento do cateto oposto: '))
cat_ad = float(input('Entre com o valor do comprimento do cateto adjacente: '))
hip = ((cat_ad**2) + (cat_op**2))**0.5
print('Para os comprimentos, dos catetos A: {} e B {}, o comprimnto da hipotenusa é: {:.2f}'.format(cat_op, cat_op, hip))

import math
hip2 = math.hypot(cat_op, cat_ad)
print('\nOutra resolução:\nA hipotenusa é {:.2f}'.format(hip2))