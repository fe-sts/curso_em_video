'''
Melhore o desafio 028.

#028 #Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para
#o usuario tentar descobrir qual foi o numero escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu
'''
import random
num_jogador = 11
cont = 0
num_comp = random.randint(0, 10)

print('\033[1;34;40m-=\033[m'*30)
print('O computador já escolheu um número de 0 a 10!')
print('\033[1;34;40m-=\033[m'*30)

while num_comp != num_jogador:
    num_jogador = int(input('Adivinhe qual foi o número: ').strip())
    print('Errou! Tente novamente ...')
    cont += 1
print('\033[1;31m-=\033[m'*30)
print('O Computador escolheu o número {}.\n'
      'Você escolheu o número {} na última tentativa.\n'
      'Foram necessárias {} tentativas para acertar!'.format(num_comp, num_jogador, cont))