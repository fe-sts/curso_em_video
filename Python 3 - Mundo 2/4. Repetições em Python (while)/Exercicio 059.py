''' ******* NÃO TERMINEI ***********
Crie um programa que leia 2 valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

print('\033[1;31mDigite 2 valores, em seguida, escolha a ação desejada: \033[m')
cont = int(0)
acao = 0

num1 = int(input('Digite o 1o valor: ').strip())
num2 = int(input('Digite o 2o valor: ').strip())

while cont != 5:
    print('\033[1;31mEscolha a ação desejada\033[m\n'
          '[1] somar\n'
          '[2] multiplicar\n'
          '[3] maior\n'
          '[4] novos numeros\n'
          '[5] sair do programa')
    acao = int(input('-->').strip())
    if acao == 1:
        print('Soma entre {} + {} = {}'.format(num1, num2, num1 + num2))
    elif acao == 2:
        print('Multiplicação entre {} x {} = {}'.format(num1, num2, num1 * num2))
    elif acao == 3:
        lista = [num1, num2]
        print('Entre {} e {}, o maior número é {}'.format(num1, num2, max(lista)))
    elif acao == 4:
        print('Novos números: ')
        num1 = int(input('Digite o 1o valor: ').strip())
        num2 = int(input('Digite o 2o valor: ').strip())
    elif acao == 5:
        cont = 5
print('FIM DO PROGRAMA')


