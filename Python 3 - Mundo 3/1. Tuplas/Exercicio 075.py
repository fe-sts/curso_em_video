'''
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''

num = (int(input('Digite um número: ').strip()),
    int(input('Digite um número: ').strip()),
    int(input('Digite um número: ').strip()),
    int(input('Digite um número: ').strip()),
    int(input('Digite um número: ').strip()))

print(f'Você digitou os valores: {num}.')
print(f'O numero 9 apareceu {num.count(9)} vezes.')

if 3 in num:
    print(f'O valor 3 apareceu na posição numero: {num.index(3)+1}')
else:
    print('Valor 3 nao foi digitado!')

print('os valores pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n)
