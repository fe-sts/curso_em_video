#Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado e a quantidade de
# dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

km = float(input('Entre com a km percorrida: '))
dias = float(input('Durante quantos dias o carro foi alugado? '))

preco = (dias * 60) + (km * 0.15)

print('Para {:.0f} dias de alguel e {} km percorrido, o valor devido é R$ {}'.format(dias, km, preco))