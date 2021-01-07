'''
Desenvolva um programa que leia o 1o termo  ea razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''

termo1 = int(input('Digite o 1o termo da PA: ').strip())
razao = int(input('Digite a razão da PA: ').strip())
#decimo = termo1 + ((10 - 1) * razao)
for c in range(1, 11):
    print('Termo {} de 10: {}'.format(c, termo1))
    termo1 += razao