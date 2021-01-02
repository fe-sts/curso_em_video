#Desenvolva um programa que pergunta a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas

dist_viagem = float(input('Digite a distância de sua viagem em km: ').strip())
if dist_viagem <= 200:
    print('O preço da passagem é R$ {}'.format(dist_viagem * 0.50))
elif dist_viagem >= 201:
    print('O preço da passagem é R$ {}'.format(dist_viagem *0.45))