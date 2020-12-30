'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu:
Preço Normal e Condição de pagamento.

- à Vista: dinheiro/cheque --> 10% de desconto
- à Vista: no cartão --> 5% de desconto
- em até 2x no cartão --> preço normal
- 3x ou mais no cartão --> 20% de juros
'''

vlr_prod = float(input('Digite o valor do produto: ').strip())
cond_pagto = int(input('\033[4;33;48mEscolha a condição de pagamento [1 a 4] \033[m:\n'
                       '[1]: à Vista: dinheiro/cheque\n'
                       '[2]: à Vista: no cartão\n'
                       '[3]: em até 2x no cartão\n'
                       '[4]: 3x ou mais no cartão\n'
                       '--> '))
if cond_pagto == 1:
    print('O valor a ser pago é R${} [10% de desconto]'.format(vlr_prod * 0.9))
elif cond_pagto == 2:
    print('O valor a ser pago é R${} [5% de desconto]'.format(vlr_prod * 0.95))
elif cond_pagto == 3:
    print('O valor a ser pago é R${} [preço normal]'.format(vlr_prod))
elif cond_pagto == 4:
    print('O valor a ser pago é R${} [20% de juros]'.format(vlr_prod * 1.2))