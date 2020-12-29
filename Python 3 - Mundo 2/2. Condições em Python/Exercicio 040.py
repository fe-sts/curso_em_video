'''Crie um programa que leia 2 notas de um aluno e calcule sua média, mostrando um mensagem no final
De acordo com a média atingida'''

nota1 = float(input("Digite sua primeira nota: ").strip())
nota2 = float(input("Digite sua segunda nota: ").strip())
media = (nota1 + nota2) / 2

if media < 5:
    print('Sua média é de {}\n \033[1;30;42m REPROVADO! \033[m.'.format(media))
elif media >= 5 and media < 7:
    print('Sua média é de {}\n \033[1;30;44m VOCÊ ESTÁ DE RECUPERAÇÃO! \033[m.'.format(media))
elif media >=7:
    print('Sua média é de {}\n \033[4;36;40m APROVADO! \033[m'.format(media))