'''
Crie um programa que leia a idade eo sexo de várias pessoas.
A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não continuar.
No final mostra:

1) quantas pessoas com mais de 18 anos.
2) quantos homens foram cadastrados.
3) quantas mulheres tem menos de 20 anos de idade.
'''
sexo = ''
idade = 0
continua = ''
mais18 = 0
homens = 0
m_menos20 = 0

while True:
    print('=-='*20)
    print(' '*20+'CADASTRO DE PESSOAS')
    print('=-='*20)
    sexo = str(input("Digite o sexo (M/F)"))
    idade = int(input("Digite a idade: "))
    continua = str(input('Deseja cadastrar outra pessoa? (S/N)'))

    if idade > 18:
        mais18 += 1
    if sexo in "Mm":
        homens += 1
    if sexo in "Ff" and idade < 20:
        m_menos20 += 1
    if continua in "Nn":
        print(f'{mais18} pessoas tem mais de 18 anos\n{homens} homens foram cadastrados\n{m_menos20} mulheres tem menos de 20 anos de idade')
        break
