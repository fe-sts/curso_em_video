'''
Crie um programa que faça o computador jogar Jokenpô contra você.
'''
import random
from time import sleep

escolha_jogador = int(input('[1] Pedra\n'
                            '[2] Papel\n'
                            '[3] Tesoura\n'
                            'Escolha a sua jogada: ').strip())
#list_comp = [1,2,3]
list_comp = random.choice([1,2,3])

if escolha_jogador == 1:
    jog = 'Pedra'
elif escolha_jogador == 2:
    jog = 'Papel'
elif escolha_jogador == 3:
    jog = 'Tesoura'

if list_comp == 1:
    computador = 'Pedra'
elif list_comp ==2:
    computador = 'Papel'
elif list_comp == 3:
    computador = 'Tesoura'

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*15)
print('COMPUTADOR JOGOU: {}\n'
      'VOCÊ JOGOU: {}'.format(computador, jog))
print('-='*15)

if escolha_jogador == list_comp:
    print('EMPATE')
elif escolha_jogador == 1 and list_comp == 2:
    print('COMPUTADOR GANHOU!')
elif escolha_jogador == 1 and list_comp == 3:
    print('VOCÊ GANHOU!')
elif escolha_jogador == 2 and list_comp == 1:
    print('VOCÊ GANHOU!')
elif escolha_jogador == 2 and list_comp == 3:
    print('COMPUTADOR GANHOU!')
elif escolha_jogador == 3 and list_comp == 1:
    print('COMPUTADOR GANHOU!')
elif escolha_jogador == 3 and list_comp == 2:
    print('VOCÊ GANHOU!')

#OUTRO JEITO DE RANDOMIZAR ESCOLHAS
itens = ('nenhum', 'Pedra', 'Papel', 'Tesoura')
computador2 = random.randint(1, 3)
print('TESTE --> O computador2 escolheu: {}'.format(itens[computador2]))