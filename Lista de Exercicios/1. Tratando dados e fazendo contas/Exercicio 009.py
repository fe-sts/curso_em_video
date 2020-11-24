#Faça um programa que leia um numero inteiro qualquer e mostre sua tabuada

n1 = int(input('Digite um numero inteiro: '))

cont_1 = 1

print('-'*12)
for cont in range(10):
    print('{} x {:2} = {:2}'.format(n1, cont_1, n1*cont_1))
    cont_1 += 1
print('-'*12)