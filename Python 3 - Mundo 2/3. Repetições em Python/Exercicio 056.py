''' *******INCOMPLETO AINDA ***********
Desenvolva um programa que leia o Nome, Idade e Sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do Homem mais velho
- Quantas mulheres tem menos de 20 anos
'''
#PRIMEIRA TENTATIVA: utilizando Dicionário

pessoas = []
idade_todas = 0
cont_id = 0
for c in range(1, 3):
    nome_novo = (input('Digite o Nome da {}ª pessoa: '.format(c)).strip())
    #nomes.append(nome_novo)
    idade_novo = int(input('Digite a Idade da {}ª pessoa: '.format(c)).strip())
    sexo_novo = (input('Digite o Sexo da {}ª pessoa (M/F): '.format(c)).strip())
    pessoas.append({'Nome': nome_novo,
                    'Idade': idade_novo,
                    'Sexo': sexo_novo}) #Cria um dicionário com os dados das pessoas

'''for i in range(1, 3):
    idade_todas += pessoas[i]['Idade']
    cont_id += 1'''
idade_media = (idade_todas/cont_id)
print('Média de idade do grupo é de: {}'.format(idade_media))

print(pessoas)
print(pessoas[1]['Idade'])


