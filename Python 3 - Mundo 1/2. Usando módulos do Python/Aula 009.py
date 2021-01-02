#Indices, Fatiamentos

lista = ['Curso em Video Python ']
#Curso em Video Python
lista[9:13] #Fatiamento--> pega da Letra V ate e
lista[9:21] #V até n
lista[9:21:2] #V até n indo de 2 em 2
lista[:5] #Inicia do caractere 0 até o 4
lista[15:] #do 15 até o final
lista[9::3] #Começa no 9 e vai até o final, pegando de 3 em 3


#Analises de Strings

len(lista) #Comprimento
lista.count('o') #conta quantas vezes a letra "o" aparece na lista
lista.count('o', 0, 13) #conta quantas vezes a letra "o" aparece na lista / verificando de 0 a 13
lista.find('deo') #quantas vezes encontra "deo" --> deo começo na posição 11
lista.find('Android') #se coloca no find uma string que nao existe na lista, retorna -1
'curso' in lista #Exista "curso" na lista? --> True/False

# Funcionalidades de Transformação
lista.replace('Python', 'Android') #Procura por Python e substitui por Android
lista.upper() #Transforma em Maiusculas
lista.lower() #Transforma em Minusculas
lista.captalize() #Pega a String inteira e deixa somente a 1a como Maiuscula
lista.title() #Faz o captalize para todas palavras
lista.strip() #Remove espaços em branco antes e depois dos caracteres
lista.rstrip() #Remove espaços da direita
lista.lstrip() ##Remove espaços da esquerda

#Funcionalidades de Divisão
lista.split() #Onde tiver espaços e cria uma divisão --> Cada palavra vira uma lista --> ficando lista dentro de outra lista

#Funcionalidades de Junção
-.join(lista) #Junta todas as listas separando por "-"

#______________________________________#

import random
#num2 = (random.randrange(0,9999))

num = str(random.randrange(1000,9999))
print(num)
print(num[0])
print(num[1])
print(num[2])
print(num[3])

print(list('teste'))

print(9//2) # entendendo o retorno da parte Inteira da divisão