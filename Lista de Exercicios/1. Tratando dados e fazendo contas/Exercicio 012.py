#Faça um algoritmo que leia o preço de um produto  e mostre  seu novo preço, com 5% de desconto.

preco = float(input('Entre com o preço do produto (Ex.: 10.50):'))

print('O preço com desconto de 5% é {:.2F}'.format(preco*0.95))