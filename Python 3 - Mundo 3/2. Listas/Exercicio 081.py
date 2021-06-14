'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
lista = []
num = 0
contador = 0
continua = ''

while True:
    num = int(input('Digite um numero: ').strip())
    lista.append(num)
    contador += 1
    continua = input('Deseja inserir outro numero? (S/N)')
    if continua in "Nn":
        break
print(f"Foram digitados {contador} numeros.")
lista.sort(reverse=True)
print(f"Os valores digitados de forma descrescente: {lista}")
if 5 in lista:
    print('O valor 5 faz parte da Lista!')
else:
    print('O valor 5 não faz parte da Lista!')

