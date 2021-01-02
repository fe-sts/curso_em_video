# Desenvolva um programa que leia 2 notas de um aluno e calcule e mostre sua média

n1 = float(input('Digite sua nota: '))
r1 = str(input('Voce tem mais alguma nota? (Responda sim ou não)'))

if r1.upper() == "SIM":
    n2 = float(input('Digite sua outra nota: '))
    print('Sua média é: {}'.format((n1+n2)/2))
elif r1.upper() == "NÃO":
    print('Sua média é: {} \n Você zerou em uma das provas!'.format((n1/2)))