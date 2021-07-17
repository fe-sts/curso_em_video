'''
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o 
(com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de 
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime, date

def calculate_age(nasc):
    today = date.today()
    return today.year - nasc.year - ((today.month, today.day) < (nasc.month, nasc.day))

dados = dict()
nasc = 0


while True:
    dados['Nome'] = input("Nome: ")
    nasc = datetime.strptime(input("Data de Nascimento (dd mm yyyy): "), "%d %m %Y")
    dados['Idade'] = calculate_age(nasc)
    dados['CTPS'] = int(input("CTPS (Digite 0 caso não tenha): "))
    if dados['CTPS'] != 0:
        dados['Ano de Contratação'] = int(input("Ano de Contratação: "))
        dados['Salario'] = float(input("Salario: "))
        dados['Aposentadoria'] = dados['Ano de Contratação'] + 35
    break

print(dados)
print('=_'*25)
for chave, valor in dados.items():
    print(f'{chave} tem o valor {valor}')