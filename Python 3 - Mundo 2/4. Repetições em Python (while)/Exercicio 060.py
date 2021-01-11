'''
Faça um programa que leia um numero qualquer e mostre o seu Fatorial.

Ex:
5! = 5x4x3x2x1 = 120
'''

num = int(input('Digite um número para saber seu fatorial: ').strip())
cont = num
fatorial = 1

print('Fatorial de {}! = '.format(num), end = '')
while cont > 0:
    print('{}'.format(cont), end = '')
    print(' x ' if cont > 1 else ' = ', end = '')
    fatorial *= cont
    cont -= 1
    #print(fatorial)
print(fatorial)