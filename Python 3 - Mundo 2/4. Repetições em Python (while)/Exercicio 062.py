'''
Melhore o Desafio 061, perguntando se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''
cont = 10
cont2 = 0
termo1 = int(input('Entre com o 1o termo da PA: ').strip())
razao = int(input('Entre com a razão da PA: ').strip())

while cont > 0:
    cont2 += 1
    print('Termo {} de 10: {}'.format(cont2, termo1))
    termo1 += razao
    cont -= 1

    if cont == 0:
        mais = str(input('Quer mostrar mais termos? [S / N]').strip())
        if mais in 'Ss':
            termo1 = int(input('Entre com o Outro 1o termo da PA: ').strip())
            cont = 10
        elif mais in 'Nn':
            print('Programa encerrado')
