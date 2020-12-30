'''
Crie um programa que faça o computador jogar Jokenpô contra você.
'''
import random
escolha_jogador = int(input('Escolha:\n'
                            '[1] Pedra\n'
                            '[2] Papel\n'
                            '[3] Tesoura\n'
                            '-->').strip())
#list_comp = [1,2,3]
list_comp = random.choice([1,2,3])

if escolha_jogador == 1:
    jog = 'Pedra'
elif escolha_jogador ==2:
    jog = 'Papel'
elif escolha_jogador == 3:
    jog = 'Tesoura'

if list_comp == 1:
    computador = 'Pedra'
elif list_comp ==2:
    computador = 'Papel'
elif list_comp == 3:
    computador = 'Tesoura'

print('COMPUTADOR ESCOLHEU: {}\n'
      'VOCÊ ESCOLHEU: {}'.format(computador, jog))

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