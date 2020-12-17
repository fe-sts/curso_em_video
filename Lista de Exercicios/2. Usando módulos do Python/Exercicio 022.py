# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1. O nome com todas as letras maiusculas
# 2. O nome com todas as letras minusculas
# 3. Quantas letras ao to do (sem considerar espaços)
# 4. Quantas letras tem o 1o nome

nome = str(input('Digite seu nome completo: '))

print('Seu nome UPPER: {}'.format(nome.upper()))
print('Seu nome lower: {}'.format(nome.lower()))
print('Nº de letras sem espaços (começo e final): {}'.format(len(nome.strip())))
print('Nº de letras sem espaços (começo, final e meio): {}'.format(len("".join(nome.split()))))
nome1 = nome[:nome.find(' ')]
print('Quantas letras tem o 1o nome {}'.format(nome1))