'''
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista 
composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada 
aluno individualmente.
'''
lista_resp = list()
lista_alunos = list()
while True:
    nome = str(input('Digite o nome do aluno: ').strip())
    n1 = float(input('Digite a Nota 1: ').strip())
    n2 = float(input('Digite a Nota 2: ').strip())
    media = (n1+n2) / 2
    lista_resp.append([nome, [n1, n2], media])
    #lista_alunos.append(lista_resp[:])
    #lista_resp.clear()
    if (input("Deseja inserir outro aluno? (S/N) ")) in "Nn":
        break

print('-'*25)
print(f'{"No.":<4}{"NOME":<15}{"MEDIA":>5}')
print('-'*25)
for chave, valor in enumerate(lista_resp):
    print(f'{chave:<4}{valor[0]:<15}{valor[2]:>5}')

while True:
    print('-'*25)
    resp = int(input("Deseja ver as notas de qual aluno? (Digite 999 para sair)").strip())
    if resp == 999:
        print("Fim da programa!")
        break
    if resp <= (len(lista_resp)-1):
        print(f'As notas de {lista_resp[resp][0]} foram: {lista_resp[resp][1]}')

'''for i in range(0, len(lista_alunos)):
    print(f'{i}   {lista_alunos[0]}   {lista_alunos[2]}')
'''

