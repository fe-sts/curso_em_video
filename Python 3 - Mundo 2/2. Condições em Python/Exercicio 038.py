'''Escreva um programa que leia 2 numeros inteiros e compare-os, mostrando na tela uma mensagem:
O 1o valor é maior
O 2o valor é maior
Não existe valo maior. São Iguais'''

num1 = int(input('Digite o 1o número: '))
num2 = int(input('Digite o 2o número: '))

if num1 > num2:
    print('O 1o valor é maior')
elif num2 > num1:
    print('O 2o valor é maior')
elif num1 == num2:
    print('Os valores são iguais.')
