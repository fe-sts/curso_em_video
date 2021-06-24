'''
Exercício Python 087: Aprimore o desafio anterior (086), mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = 0
soma_col_3 = 0
maior_lin_2 = []

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um numero para [{l}, {c}]: "))
        soma += matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
    print()

#A) A soma de todos os valores pares digitados.
print(f'A soma de todos os valores pares digitados: {soma}')

#B) A soma dos valores da terceira coluna.
for i in range(0,3):
    #print(matriz[i][2])
    soma_col_3 += matriz[i][2]
print(f'A soma dos valores da terceira coluna: {soma_col_3}')

#C) O maior valor da segunda linha.
for i in range(3):
    maior_lin_2.append(matriz[1][i])
print(f'O maior valor da segunda linha: {max(maior_lin_2)}')
