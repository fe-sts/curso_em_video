'''Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou de tempo.
'''
import datetime
ano = int(input("Digite seu ano de nascimento: "))
ano_atual = datetime.date.today().year
idade = ano_atual - ano

if idade == 18:
    print('Você precisa de alistar este ano!')
elif 18 > idade:
    print('Faltam {} anos para se alistar'.format(18 - idade))
    print('Seu alistamento será em {} '.format((18 - idade) + ano_atual))
elif idade > 18:
    print('\033[1;34;40mJá passou {} anos de seu tempo de alistamento \033[m'.format(idade - 18))
    print('Seu ano de alistamento foi em {}'.format(ano_atual - (idade - 18)))
