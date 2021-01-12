'''
Refaça o desafio 051, utlizando while:

Desenvolva um programa que leia o 1o termo  ea razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''

termo1 = int(input('Entre com o 1o termo da PA: ').strip())
razao = int(input('Entre com a razão da PA: ').strip())
cont = 10
cont2 = 0
while cont > 0:
    cont2 += 1
    print('Termo {} de 10: {}'.format(cont2, termo1))
    termo1 += razao
    cont -= 1