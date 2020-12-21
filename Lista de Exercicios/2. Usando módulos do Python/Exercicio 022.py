# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1. O nome com todas as letras maiusculas
# 2. O nome com todas as letras minusculas
# 3. Quantas letras ao to do (sem considerar espaços)
# 4. Quantas letras tem o 1o nome

nome = str(input('Digite seu nome completo: '))
#1
print('Seu nome UPPER: {}'.format(nome.upper()))

#2
print('Seu nome lower: {}'.format(nome.lower()))

#3
print('Nº de letras sem espaços (começo e final): {}'.format(len(nome.strip())))
print('Nº de letras sem espaços (começo, final e meio): {}'.format(len("".join(nome.split()))))
print('Nº de letras sem espaços (começo, final e meio)(Outro jeito): {}'.format(len(nome) - nome.count(' ')))

#4
nome1 = nome[:nome.find(' ')]
print('Quantas letras tem o 1o nome {}'.format(len(nome1)))
print('Quantas letras tem o 1o nome {} (Outro jeito)'.format(nome.find(' ')))
separado_1 = nome.split()
print('Quantas letras tem o 1o nome {} (Jeito 3)'. format(separado_1[0]))