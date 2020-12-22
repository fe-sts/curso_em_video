#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para
#o usuario tentar descobrir qual foi o numero escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
num_comp = randint(0, 5)
print(num_comp)
num_usuario = int(input('O Computador escolheu um numero de 0 a 5.\nAdivinhe qual foi: '))

if num_usuario <= 5:
    if num_usuario == num_comp:
        print('Acertou miseravi!\nnumero computador: {}\nseu numero: {}'.format(num_comp, num_usuario))
    else:
        print('Errou!\nnumero computador: {}\nseu numero: {}'.format(num_comp, num_usuario))
elif num_usuario > 5:
    print('Você digitou um numero que não está no jogo!')