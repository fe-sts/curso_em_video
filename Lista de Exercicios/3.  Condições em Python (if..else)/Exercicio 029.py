#Escreva um programa que leia a velocidade de um carro;
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite

velocidade = float(input('Qual sua velocidade em km/h? '))
if velocidade > 80:
    multa = (velocidade -80) * 7
    print('ACIMA DA VELOCIDADE PERMITIDA!\nVocê vai receber uma multa de R$ {}'.format(multa))
else:
    print('Você está dentro do limite de velocidade.')