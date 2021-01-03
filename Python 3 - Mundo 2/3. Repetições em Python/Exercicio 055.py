'''
Faça um programa que leia o peso de 5 pessoas.
No final, mostre qual foi o maior eo menor peso lidos.
'''
maior = 0
menor = 500
print('Digite os Pesos:\n', end = '')
for c in range(1, 6):
    peso = float(input('{}ª pessoa: '.format(c)).strip())
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso foi: {}'. format(maior))
print('O menor peso foi: {}'. format(menor))