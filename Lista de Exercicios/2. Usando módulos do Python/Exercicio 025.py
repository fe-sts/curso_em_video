#Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome

nome = str(input('Digite um nome: '))
nome_mai = nome.upper()
if ('SILVA' in nome_mai) == True:
    print('Tem Silva no nome')
else:
    print('não tem Silva no nome')

#Outro jeito
nome2 = str(input('Qual seu nome(2)?: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome2.upper()))