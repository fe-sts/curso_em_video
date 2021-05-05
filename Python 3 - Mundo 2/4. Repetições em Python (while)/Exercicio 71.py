'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No inicio, pergunte ao usuario qual será o Valor a ser sacado (numero inteiro) eo programa vai informar quantas
cédulas de cada valor serão entregues.
Considere que o caixa possui cédulas de 50, 20, 10 e 1 real.
'''



print("=======Sistemas Caixa Eletrônico========")
valor = int(input('Qual valor deseja sacar? R$').strip())
total = valor
cedula = 50
total_cedula = 0

while True:
    if total >=cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} de {cedula}')
        if cedula == 50:
            cedula == 20
        elif cedula == 20:
            cedula == 10
        elif cedula == 10:
            cedula == 1
        total_cedula = 0
        if total_cedula == 0:
            break
    '''
    valor = int(input('Qual valor deseja sacar? R$').strip())

    if valor // 50 > 1:
        nota50  = valor // 50
        print(f'Notas de 50: {nota50}')
    '''
