#Escreva um programa que leia um valor em metros eo exiba convertido em centímetros e em milimetros

n1 = float(input('Entre com o valor em metros (use .(ponto) para valores quebrados):'))

print('Para o valor {} m \n Equivale a: \n {} centímetros \n {} milímetros'.format(n1, n1*(100), n1*(1000)))