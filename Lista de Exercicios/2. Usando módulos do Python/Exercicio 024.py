#Crie um programa que leia o nome de uma cidade e diga se ela começa com a palavra SANTO

cidade = str(input('Digite o nome de sua cidade: '))
santo = cidade.upper()
#verifica = ('SANTO' in santo)

if ('SANTO' in santo) == True:
    print('Cidade começa com SANTO')
else:
    print('cidade Não começa com SANTO')


#cidade2 = list(input('Digite o nome de sua cidade lista: '))
#print(cidade2[1].upper())
