'''
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um 
sistema de visualização de detalhes do aproveitamento de cada jogador'''

'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

info = dict()
num = 0
gols = list()
total = 0
time = list()

while True:
    info.clear()
    info["Nome"] = input("Nome: ")
    num = int(input("Quantas partidas o jogador X jogou? "))
    for gol in range(num):
        gols.append(int(input(f"Quantos gols na partida {gol+1}? ")))
    info["Gols"] = gols
    info["Total"] = sum(gols)
    time.append(gols.copy)

    while True:
        resp = str(input("Quer cotinuar? (S/N) ").upper()[0])
        if resp in 'SN':
            break
        else:
            print('ERRO! Digite S ou N.')
    if resp == 'N':
        break




print("-+"*30)
print(info)
print("-+"*30)
for chave, valor in info.items():
    print(f'o campo: {chave}, tem o valor: {valor}')
print("-+"*30)
print(f' O jogador {info["Nome"]} marcou {info["Total"]} gols.')
for indice, valor in enumerate(info["Gols"]):
    print(f'    ==> Na partida {indice+1}, fez {valor} gols.')