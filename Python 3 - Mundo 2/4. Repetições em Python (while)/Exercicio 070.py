'''
Crie um programa que leia o Nome eo Preço de varios produtos.
O programa deverá perguntar se o usuário vai continuar.
o final, mostre:

a) Qual é o Total gasto na compra
b) Quantos produtos custam mais de R$1000
c) Qual é o nome do produto mais barato.
'''

print('==='*30)
print(' '*20+'SISTEMA CADASTRO SIMPLES')
print('==='*30)

lista = []
nome = ''
preco = 0.0
total = 0.0
mais1000 = 0.0
continua = ''
while True:
    nome = str(input('Digite o Nome do produto: ').strip())
    preco = float(input('Digite o Preço do produto: ').strip())
    total += preco

    if not lista:
            dicio_produtos = {"Nome: ": nome, "Preço: ": preco}
            lista.insert(0, dicio_produtos)
    else:
        if preco < lista[0]["Preço: "]:
            dicio_produtos = {"Nome: ": nome, "Preço: ": preco}
            lista.insert(0, dicio_produtos)
    if preco > 1000:
        mais1000 += 1
    
    continua = str(input('Quer continuar? (S/N)'))
    if continua in 'Nn':
        break

print(f'O Total gasto na compra foi R${total}')
print(f'A quantidade de produtos que custam mais que R$1000 foi {mais1000}')
print(f'O produto mais barato foi ***{lista[0]["Nome: "]}*** com o preço de R${lista[0]["Preço: "]}')