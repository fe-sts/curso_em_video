'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 

No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

'''
num = 0
lista = []
for cont in range(0,5):
    num = int(input(f"Digite um numero para a posição {cont}: "))
    lista.append(num)

print(f'O maior numero digitado foi: {max(lista)} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i} | ', end='')

print(f'\nO menor numero digitado foi: {min(lista)} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i} | ', end='')
