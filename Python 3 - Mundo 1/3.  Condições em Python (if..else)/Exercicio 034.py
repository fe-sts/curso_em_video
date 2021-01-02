#Faça um programa que leia o salario de um funcionário
# Se tiver um salario acima de R$1250, tem 10% de aumento
# Se for abaixo, tem %15 de aumento

salario = float(input('Entre com o salario: ').strip())

if salario > 1250:
    print('O novo salario é de {:.2f}'.format(salario * 1.1))
elif salario <= 1250:
    print('O novo salario é de {:.2f}'.format(salario * 1.15))

#if | elif | float