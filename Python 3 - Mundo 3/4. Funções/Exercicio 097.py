'''
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer 
como parâmetro e mostre uma mensagem com tamanho adaptável.
 Ex:
    escreva(‘Olá, Mundo!’) Saída: 
    ~~~~~~~~~
    Olá, Mundo!
    ~~~~~~~~~'''

def palavra(msg):
    tamanho = len(msg) + 6
    print('~'*tamanho)
    print(f'   {msg}')
    print('~'*tamanho)


palavra('Felipe')
palavra('Rinaldini')
palavra('Santos')
palavra('Frase teste longa!')