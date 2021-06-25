'''
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.
'''

'''
# RESOLUÇÃO 1

from random import randint

num_jogos = 0
num = 0
lista_jogo = []
lista_conjuto = []

num_jogos = int(input('Quantos jogos deseja fazer para Megasena? ').strip())
cont = 0

for i in range(num_jogos):
    for l in range(6):
        num = randint(1, 60)
        if num not in lista_jogo:
            lista_jogo.append(num)
        else:
            num = randint(0, 60)
            lista_jogo.append(num)
    lista_conjuto.append(lista_jogo[:])
    lista_jogo.clear()
print(lista_conjuto)
'''

#RESOLUÇÃO 2

from random import randint

num_jogos = 0
num = 0
lista_jogo = []
lista_conjuto = []

num_jogos = int(input('Quantos jogos deseja fazer para Megasena? ').strip())
total = 1
while total <= num_jogos:
    cont = 0
    total += 1
    while True:
        num = randint(1, 60)
        if num not in lista_jogo:
            lista_jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    lista_jogo.sort()
    lista_conjuto.append(lista_jogo[:])
    lista_jogo.clear()
    
for chave, valor in enumerate(lista_conjuto):
    print(f'Jogo: {chave+1}: {valor}')