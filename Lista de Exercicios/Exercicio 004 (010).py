#Crie um programa que leia quanto dinheiro um apessoa tem na carteira e mostre quantos doleres ela pode comprar

n1 = float(input('Digite quanto dinheiro você tem na carteira (Em reais R$): '))
n2 = n1/5.46

print('Com {} reais, você consegue  comprar {} dolares'.format(n1, n2))