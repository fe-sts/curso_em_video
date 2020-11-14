#Faça um programa que leia um numero interio qualquer e mostre sua tabuada

n1 = int(input('Digite um numero inteiro: '))

cont_1 = 1


for cont in range(10):
    print('{} x {} = {}'.format(n1, cont_1, n1*cont_1))
    cont_1 += 1