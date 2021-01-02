'''
Refaça o desafio 009
#Faça um programa que leia um numero inteiro qualquer e mostre sua tabuada
'''

num = int(input('Digite um numero para saber sua tabuada: ').strip())

for c in range(0, 11):
        print('{} X {} = {}'.format(c, num, (c * num)))