'''
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from time import sleep
from random import randint
from operator import itemgetter
from collections import OrderedDict

jogos = dict()
num_sorteado = 0
ranking = list()

for i in range(5):
    jogador = str("jogador " + str(i+1))
    num_sorteado = randint(1, 6)
    jogos[jogador] = num_sorteado

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
#ranking = OrderedDict(sorted(jogos.items(), key=lambda x: x[1]))

for chave, valor in jogos.items():
  print(f'{chave} tirou {valor}')
  sleep(0.5)
print("=-"*25)
for chave, valor in enumerate(ranking):
  print(f'{chave+1}º lugar: {valor[0]} com {valor[1]}')
  sleep(0.2)
