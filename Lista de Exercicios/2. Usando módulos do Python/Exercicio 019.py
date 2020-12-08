#Um professor quer sortear um dos seus 4 alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles
import random
n_aluno = int(1)
alunos = []
for a in range(4):
    alunos.append(input('Digite o nome do aluno numero {} :'.format(n_aluno)))
    n_aluno += 1
#alunos.extend(input('Digite o nome dos alunos separados por virgula (,): ')) #nao funciona pois cada letra vira uma instância dentro da lista
print('{}'.format(random.choice(alunos)))