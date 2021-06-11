'''
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 

Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

'''

palavras = ('sagaz', 'negro', 'amago', 'exito', 'mexer', 'termo', 'algoz', 'senso', 'nobre', 'python', 'kotlin')


for i in palavras:
    print(f'\nA palavra "{i}"" contem as vogais: ', end='')
    for letra in i:
        if letra in "aeiouAEIOU":
            print(f'{letra.upper()}', end=' ')

