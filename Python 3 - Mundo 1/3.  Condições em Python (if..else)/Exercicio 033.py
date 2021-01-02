#Faça um programa que leia 3 numeros.
#Mostre qual é o maior eo menor

n1 = int(input('Digite a 1o numero: '))
n2 = int(input('Digite a 2o numero: '))
n3 = int(input('Digite a 3o numero: '))

#Achar maior
if n1 >= n2:
    if n1 >= n3:
        maior = n1
        print('Maior: n1 > n3: {}'.format(maior))
    elif n1 < n3:
        maior = n3
        print('Maior n1 < n3: {}'.format(maior))
elif n1 < n2:
    if n2 >= n3:
        maior = n2
        print('Maior n2 > n3: {}'.format(maior))
    elif n3 >= n2:
        maior = n3
        print('Maior n3 > n2: {}'.format(maior))

#Acha menor
if n1 <= n2:
    if n1 <= n3:
        menor = n1
        print('Menor: n1 < n3: {}'.format(menor))
    elif n1 > n3:
        menor = n3
        print('Menor: n1 > n3: {}'.format(menor))
elif n1 > n2:
    if n2 <= n3:
        menor = n2
        print('Menor n2 < n3: {}'.format(menor))
    elif n3 <= n2:
        menor = n3
        print('Menor n3 < n2: {}'.format(menor ))

#OUTRO JEITO
#Menor numero
menor2 = n1
if n2 < n3 and n2 < n1:
    menor2 = n2
    print('Menor numero digitado foi: {}'.format(menor2))
if n3 < n1 and n3 < n2:
    menor2 = n3
    print('Menor numero digitado foi: {}'.format(menor2))

#Maior numero
maior2 = n1
if n2 > n1 and n2 > n3:
    maior2 = n2
    print("Maior numero digitado foi: {}".format(maior2))
if n3 > n1 and n3 > n2:
    maior2 = n3
    print('Maior numero digitado foi: {}'.format(maior2))