'''
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores 
ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

'''
lista_pares = []
lista_impares = []
lista = []
continua = ''
while True:
    resposta = int(input("Digite um numero: "))
    lista.append(resposta)
    continua = input('Deseja contiuar? (S/N)')
    if continua in 'Nn':
        break

for indice, valor in enumerate(lista):
    #print(f'Indice {indice}')
    #print(f'Valor {valor}')
    if valor % 2 == 0:
        lista_pares.append(valor)
    else:
        lista_impares.append(valor)

print(f' Lista completa: {lista}')
print(f' Lista com Pares: {lista_pares}')
print(f' Lista com Impares: {lista_impares}')
