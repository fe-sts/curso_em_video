'''
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria de acordo com a idade.
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Senior
- Acima de 20 anos: Master
'''

idade = int(input('Digite a idade do atleta: ').strip())
if  idade <= 9:
    print("Mirim")
elif idade > 9 and idade <=14:
    print('Infantil')
elif idade > 14 and idade <=19:
    print('Junior')
elif idade == 20:
    print('Senior')
elif idade  > 20:
    print('Master')