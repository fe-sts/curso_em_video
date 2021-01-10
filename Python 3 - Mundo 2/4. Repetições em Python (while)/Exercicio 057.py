'''
Faça em programaque leia o Sexo de uma pessoa, mas só aceite os valores 'M' e 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite seu sexo (M|F): ').upper()
    if sexo != 'M' and sexo != 'F':
        print('Tente novamente!')
print('Fim')