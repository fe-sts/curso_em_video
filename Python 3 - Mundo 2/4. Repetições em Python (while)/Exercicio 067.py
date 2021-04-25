'''
Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para o valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for Negativo.
'''

num = 0
while True:
    num = int(input('Digite o numero que quer saber a tabuada: '))
    if num < 0:
        print('Fim do programa!')
        break
    for i in range(11):
        print(f'{i} X {num} = {i*num}')
