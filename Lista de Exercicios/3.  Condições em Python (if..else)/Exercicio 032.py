#Faça um programa que leia um ano qualquer e mostre se ele é bissexto

ano = int(input('Digite o ano para saber se é Bissexto: '))
if (ano % 4) == 0:
    if ((ano % 100) != 0) or (ano % 400) == 0:
        print('O ano {} é bissexto!'.format(ano))
else:
    print("O ano {} não é bissexto.".format(ano))