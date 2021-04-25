'''
Faça um programa que jogue Par ou Impar com o computador.
O jogo só será interrompido quando o jogador Perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randrange

num = 0
tipo = ''
num_comp = 0
resultado = ''
vitorias = 0

print('='*60)
print('JOGO IMPAR OU PAR')
print('='*60)
while True:
    num = int(input('Digite um numero:'))
    tipo = str(input('Escolha se é Par ou Impar (P/I): '))
    num_comp = randrange(999)

    if tipo in "Pp":
        tipo = "Par"
    elif tipo in "Ii":
        tipo = "Impar"

    if (num + num_comp) % 2 == 0:
        resultado = 'Par'
    elif (num + num_comp) % 2 == 1:
        resultado = 'Impar'
    
    if tipo == resultado:
        print('Você ganhou!')
        vitorias += 1
    else:
        print(resultado)
        print('Você Perdeu!')
        print(f'Você venceu {vitorias} vezes!')
        break
  
