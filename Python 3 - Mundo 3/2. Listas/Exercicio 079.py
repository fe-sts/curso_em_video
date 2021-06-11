'''
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
lista = []
num = 0
continua = ''
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Você já digitou este valor. Não será adicionado!')
    else:
        lista.append(num)
    continua = input('Quer inserir outro numero? (S/N): ')
    if continua in "Nn":
        break
print("Os valores em ordem crecente são: {}".format(sorted(lista)))