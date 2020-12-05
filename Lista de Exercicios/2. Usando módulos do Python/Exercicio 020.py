#O mesmo professor do exercicio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos alunos e mostre a ordem que vão apresentar
import random
alunos = []
cont_aluno = 1
for a in range(4):
    alunos.append(input('Digite o nome do aluno {}: '.format(cont_aluno)))
    cont_aluno += 1

random.shuffle(alunos)
print(alunos)