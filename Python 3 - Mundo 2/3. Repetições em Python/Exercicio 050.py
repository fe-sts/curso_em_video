'''
Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas dos pares.
Se o valor digitado for impar, desconsidere-o.
'''

soma = 0
for c in range(1, 7):
    num = int(input("Digite o {}º número inteiro: ".format(c)).strip())
    if (num % 2) == 0:
        soma += num
print('A soma dos números pares é {}'.format(soma))