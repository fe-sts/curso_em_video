'''
Desenvolva um programa que leia o Nome, Idade e Sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do Homem mais velho
- Quantas mulheres tem menos de 20 anos
'''
pessoas = []
todas_idades = 0
h_velho = 0
m_20 = 0
sexo_pessoa = ''

for c in range(1, 5):
    nome_novo = (input('Digite o Nome da {}ª pessoa: '.format(c)).strip())
    idade_novo = int(input('Digite a Idade da {}ª pessoa: '.format(c)).strip())
    sexo_novo = (input('Digite o Sexo da {}ª pessoa (M/F): '.format(c)).strip())
    pessoas.append({'Nome': nome_novo,
                    'Idade': idade_novo,
                    'Sexo': sexo_novo}) #Cria um dicionário com os dados das pessoas
    print('*' * 60)

for i in range(0, len(pessoas)):
    sexo_pessoa = pessoas[i]['Sexo']
    if sexo_pessoa == 'M':
        if (pessoas[i]['Idade']) >= todas_idades: #Pega a Idade do homem mais velho
            h_velho = pessoas[i]['Idade']
    elif sexo_pessoa == 'F':
        if (pessoas[i]['Idade']) < 20: #Quantas mulheres com menos de 20 anos
            m_20 += 1
    todas_idades += pessoas[i]['Idade'] #Soma as idades de todas as pessoas

idade_media = todas_idades / len(pessoas) #Calcula a média de idade do grupo
print('-='*60)
print('A idade média das {} pessoas é: {}'.format((len(pessoas)), idade_media))
print('A idade do homem mais velho é: {}'.format(h_velho))
print('A quantidade de mulheres com menos de 20 anos é: {}'.format(m_20))
print('-='*60)
