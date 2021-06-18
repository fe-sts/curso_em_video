'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.         
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

aux = []
principal = []
maior = menor = 0

while True:
    aux.append(input('Nome: '))
    aux.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = aux[1]
    else:
        if aux[1] > maior:
            maior = aux[1]
        if aux[1] < menor:
            menor = aux[1]

    principal.append(aux[:])
    aux.clear()
    continua = input('Quer continuar? (S/N) ')
    if continua in "Nn":
        break
#
print(f'Existem {len(principal)} cadastros.')
print(f'O menor peso foi: {menor}. Peso de: ', end='')
for i in principal:
    if i[1] == menor:
        print(i[0])
print(f'O maior peso foi: {maior}. Peso de: ', end='')
for i in principal:
    if i[1] == maior:
        print(i[0])
