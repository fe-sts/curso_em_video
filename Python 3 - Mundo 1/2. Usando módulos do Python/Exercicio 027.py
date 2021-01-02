#Faça um programa que leia o nome completo de um a pessoa, mostrando em seguida o primeiro eo ultimo
#nome separadamente.
#Ex. Ana Maria de Souza
#primeiro = Ana | ultimo = Souza

nome = str(input("Digite seu nome completo: ")).strip()
nome_separado = nome.split()
print('Seu primeiro nome é: {}'.format(nome_separado[0]))
print('Seu ultimo nome é {}'.format(nome_separado[len(nome_separado) - 1]))