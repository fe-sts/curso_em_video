'''
Exercício Python 094: 
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um 
dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres
 D) Uma lista de pessoas com idade acima da média'''

conjunto = dict()
lista = list()
soma_idade = 0

while True:
    conjunto["nome"] = input("Nome: ")
    while True:
        conjunto["sexo"] = input("Sexo [M/F]: ")
        if conjunto["sexo"] in "MmFf":
            break
        else:
            print("ERRO: Digite M ou F")
    conjunto["idade"] = int(input("Idade: "))
    soma_idade += conjunto["idade"]
    lista.append(conjunto.copy())
    cont = input("Quer continuar? [S/N] ")
    if cont in "Nn":
        break
    
print(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
media = soma_idade/len(lista)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) A lista de pessoas que estão acima da média: ')
for indice, valor in enumerate(lista):
    if valor["idade"] > media:
        print(f'nome = {valor["nome"]}' f'; sexo = {valor["sexo"]}' f' idade = {valor["idade"]}')
