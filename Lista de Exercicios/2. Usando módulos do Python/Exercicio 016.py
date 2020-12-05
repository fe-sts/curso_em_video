#Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção Inteira
#Ex.: 6,16 --> 6

import math
n1 = float(input('Digite um numero: '))
inteiro = math.trunc(n1) #truncado
print('Para o numero inserido {}, sua porção Inteira é: {}'.format(n1, inteiro))
print('Outro metodo para ficar Inteiro {:.0f}'.format(n1))
fabs = math.fabs(n1)
print('Outro metodo para ficar Inteiro 2 {}'.format(fabs))