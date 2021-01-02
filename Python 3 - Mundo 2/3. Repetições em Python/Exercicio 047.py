'''
Faça um programa que mostre todos os numeros pares entre 1 e 50.
'''
from time import sleep
for c in range(1, 50):
    if (c % 2) == 0:
        print('Numero par: {}'.format(c))
        sleep(0.5)