'''
Faça um programa que calcule a soma de todos os numeros impares que são multiplos de 3 e que se encontram no
intervalos entre 1 até 500.
'''

soma = 0
cont = 0
for c in range(1, 501):
    if (c % 2) == 1:
        if (c % 3) == 0:
            soma += + c
            cont += 1
print('Total da soma: {}'.format(soma))
print('Foram somados {} números'.format(cont))