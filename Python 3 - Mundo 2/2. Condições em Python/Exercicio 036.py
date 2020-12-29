'''Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da Casa, o Salário do comprador e em quantos Anos ela vai pagar.
Calcule o valor da prestação mensal, sabendo que não pode exceder 30% do salario, senão o emprestimo serpa negado.
'''
from math import ceil
valor_casa = float(input('Digite o valor da casa: ').strip())
salario = float(input('Digite o valor de seu salário: ').strip())
anos_pgto = int(input('Digite em quantos anos você quer pagar: ').strip())

prestacao = valor_casa / (anos_pgto * 12)

if prestacao > (salario * 0.3):
    print('EMPRESTIMO NEGADO!\n Excede 30% de seus rendimentos!')
else:
    print('\033[4;35;40m OK! EMPRESTIMO APROVADO! \033[m')
    print('O valor de sua prestação mensal será de \033[1;36;40m R${} \033[m'.format(ceil(prestacao)))

