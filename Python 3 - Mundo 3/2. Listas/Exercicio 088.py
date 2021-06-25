'''
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.
'''
from random import randint

num_jogos = 0
num = 0
lista_jogo = []
lista_conjuto = []
'''
while True:
    num_jogos = int(input('Quantos jogos deseja fazer para Megasena? ').strip())
    for megasena in range(num_jogos):
'''
num_jogos = int(input('Quantos jogos deseja fazer para Megasena? ').strip())
 
for j in range(num_jogos):
    for i in range(6):
        num = randint(0, 60)
        lista_jogo.append(num)
    lista_conjuto.append(lista_conjuto)

for l in range(len(lista_conjuto)):
    print(lista_conjuto[l][l])
#print(lista_jogo)
