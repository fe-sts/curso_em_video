'''
Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros
elementos de uma Sequencia de Fibonacci.
Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

{\displaystyle F_{n}=F_{n-1}+F_{n-2},}
'''

termo_fibo = int(input('Digite quanto termos desejado da Sequência de Fibonacci: ').strip())
cont = termo_fibo
cont2 = 0
fibo = 0
zero = 0
um = 1

while fibo < termo_fibo:
    print(fibo)
    fibo = fibo + zero
    zero = fibo - zero
    if fibo == 0:
        fibo = fibo + 1








'''while cont2 != termo_fibo:
    if fibo == 0:
        print('{} -> '.format(fibo), end='')
        fibo += 1
    elif fibo == 1:
        print('{} -> '.format(fibo), end='')
        fibo += 1
        um = 1
        if um == 1:
            print('{} -> '.format(1), end='')
            um += 1
    elif fibo == 2:
        print('{} -> '.format('Aqui'), end = '')
        fibo += 1'''
    #cont2 += 1

