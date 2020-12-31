'''Escreva um programa que leia um numero inteiro qualquer a peça para o usuarioescolher qual será a base de
conversão:
1: binário
2: octal
3: hexadecimal'''

num = int(input('Digite um numero inteiro: ').strip())
base = int(input('Escolha a base para qual quer converter'
                 '\n [1]: binário'
                 '\n [2]: octal'
                 '\n [3]: hexadecimal'
                 '\n---> '))
if base == 1:
    print('Base Binária = \033[1;35;40m {} \033[m'.format(bin(num)[2:]))
elif base == 2:
    print('Base Octal = \033[1;31;40m {} \033[m'.format(oct(num)[2:]))
elif base == 3:
    print('Base Hexadecimal = \033[1;31;42m {} \033[m'.format(hex(num)[2:]))
else:
    print('Opção inválida.')