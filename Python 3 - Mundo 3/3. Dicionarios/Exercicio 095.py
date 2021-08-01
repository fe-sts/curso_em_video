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
cod = 0

while True:
    info.clear()
    info["Nome"] = input("Nome: ")
    num = int(input("Quantas partidas o jogador X jogou? "))
    for gol in range(num):
        gols.append(int(input(f"Quantos gols na partida {gol+1}? ")))
    info["Gols"] = gols[:]
    info["Total"] = sum(gols)
    time.append(info.copy())
    del gols[:]

    while True:
        resp = str(input("Quer cotinuar? (S/N) ").upper()[0])
        if resp in 'SN':
            break
        else:
            print('ERRO! Digite S ou N.')
    if resp == 'N':
        break
    

print("-="*30)
print("cod ", end='')
for indice in info.keys():
    print(f'{indice:<15}', end='')
print()
print("--"*30)

for indice, valor in enumerate(time):
    print(f'{indice:>2} {valor["Nome"]:<15} {valor["Gols"]} {valor["Total"]:>10}')

while True:
    cod = int(input("Deseja ver os dados de qual jogador? (999 para sair)"))
    if cod == 999:
        print("Fim programa.")
        break
    if cod >= len(time):
        print(f"ERRO! Escolha um jogador existente. Não existe o indice {cod}")
    else:
        print(f' -- DADOS DO JOGADOR: {time[cod]["Nome"]}')
        for indice, valor in enumerate(time[cod]["Gols"]):
            print(f'     No jogo {indice+1} fez {valor} gols.')
        print("-"*40)
