'''
Faça um programa que mostre todos os numeros pares entre 1 e 50.
'''
from time import sleep
for c in range(1, 51):
    if (c % 2) == 0:
        print('Numero par: {}'.format(c))
        sleep(0.1)

#OUTRO JEITO --> Consumindo menos processamento!
for n in range(2, 51, 2): #pulando de 2 em 2
    print(n, end = ' ')
print('Acabou')