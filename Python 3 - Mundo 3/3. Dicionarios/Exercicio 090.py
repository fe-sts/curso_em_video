'''
Exercício Python 090: Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.
'''
'''dicionario = {}
dicionario["Nome"] = input("Nome: ")
dicionario["Media"] = float(input(f'Média de {dicionario["Nome"]}: '))

print("=-="*30)
print(f'Nome igual a {dicionario["Nome"]}')
print(f'Média é igual a {dicionario["Media"]}')
if dicionario['Media'] >= 7:
    dicionario["Situacao"] = "Aprovado"
else:
    dicionario["Situacao"] = "Não aprovado"
print(f'Situação é igual a {dicionario["Situacao"]}')'''

#OUTRA RESOLUÇÃO:
dicionario = {}
dicionario["Nome"] = input("Nome: ")
dicionario["Media"] = float(input(f'Média de {dicionario["Nome"]}: '))
if dicionario['Media'] >= 7:
    dicionario["Situacao"] = "Aprovado"
else:
    dicionario["Situacao"] = "Não aprovado"
print("=-="*30)
for chave, valor in dicionario.items():
    print(f'{chave} é igual a {valor}')
