'''
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos 
preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

'''
listas = ('Lápis', 1.70,
          'Borracha', 2,
          'Caneta', 3.2,
          'Mochila', 32,
          'Livro', 15)

print('-'*40)
print(f'{"Lista de Preços":^40}')
print('-'*40)
for posicao in range(0, len(listas)):
    if posicao % 2 == 0:
        print(f'{listas[posicao]:.<30}', end='') #30 posições | alinhado a esquerda < | preenchido com pontos '.'
    else:
        print(f'R${listas[posicao]:>6.2f}') # 6 posições | 2f são 2 casas decimais
print('-'*40)