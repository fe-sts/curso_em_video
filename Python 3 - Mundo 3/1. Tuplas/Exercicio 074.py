'''
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na 
tupla.
'''
import random

numeros = (random.randint(1,10),random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))

print('Os numeros sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')

print(f'\nO maior valor sorteado foi: {max(numeros)}')

print(f'O menor valor sorteado foi: {min(numeros)}')
