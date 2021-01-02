#Crie um programa que leia o nome de uma cidade e diga se ela começa com a palavra SANTO

cidade = list(input('Digite o nome de sua cidade: '))
#santo = cidade.upper()
#verifica = ('SANTO' in santo)


santo = ''.join(map(str, cidade[0:6]))
santo_m = santo.upper()
if ('SANTO' in santo_m) == True:
    print('tem SANTO no começo!')
else:
    print('não tem Santo no começo')

#if ('SANTO' in santo) == True:
#    print('Cidade começa com SANTO')
#else:
#    print('cidade Não começa com SANTO')


#cidade2 = list(input('Digite o nome de sua cidade lista: '))
#print(cidade2[1].upper())

#Outro jeito
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')