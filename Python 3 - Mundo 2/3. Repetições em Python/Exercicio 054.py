'''
Crie um programa que leia o ano de nascimento de 7 pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade a quantas já são maiores.
'''
cont_maior = 0
cont_menor = 0
for c in range(1, 8):
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)).strip())
    if idade >= 21:
        cont_maior += 1
    elif idade < 21:
        cont_menor += 1
print('='*50)
print('{} pessoas tem 21 anos ou mais'.format(cont_maior))
print('{} pessoas tem menos de 21 anos'.format(cont_menor))