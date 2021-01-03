'''
Faça um programa que leia um numero inteiro e diga se ele é ou não
um numero primo.
'''

num = int(input('Digite um numero inteiro para saber se ele é primo: '))
contador = 0
for cont in range(1, num + 1):
    if (num % cont) == 0:
        contador += 1
        print('\033[1:35:48m É divisível por: \033[m', end = '')
        print('{}'.format(cont))
print('O número {} foi divisível {} vezes'.format(num, contador))

if contador == 2:
    print('Então, ele é Primo!')
else:
    print('Então ele não é Primo!')