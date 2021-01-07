'''
Crie um programa que leia o ano de nascimento de 7 pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade a quantas já são maiores.
'''
import datetime
cont_maior = 0
cont_menor = 0
ano_atual = datetime.date.today().year
'''data_atual = datetime.datetime.now()
ano_atual = int(data_atual.strftime('%Y'))'''#Converte String em Inteiro

for c in range(1, 8):
    ano_nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)).strip())
    if ano_atual - ano_nasc >= 21:
        cont_maior += 1
    elif ano_atual - ano_nasc < 21:
        cont_menor += 1
print('='*50)
print('{} pessoas tem 21 anos ou mais'.format(cont_maior))
print('{} pessoas tem menos de 21 anos'.format(cont_menor))
