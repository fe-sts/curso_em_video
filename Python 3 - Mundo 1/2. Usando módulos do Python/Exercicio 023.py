#Faça um programa que leia de 0 a 0000 e mostre na tela cada um dos digitos separadamente.
#numero: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

import random
num = int(random.randrange(0,9999))
#numero = list(input('Numero aleatório de 0 a 9999: {} '.format()))

print(type(num))

print('Numero aleatório de 0 a 9999: {}'.format(num))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
print(num%1000)

