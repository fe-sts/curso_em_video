#Faça um programa que leia 3 numeros.
#Mostre qual é o maior eo menor

n1 = int(input('Digite a 1o numero: '))
n2 = int(input('Digite a 2o numero: '))
n3 = int(input('Digite a 3o numero: '))

#Achar maior
if n1 >= n2:
    if n1 >= n3:
        maior = n1
        print('Maior: n1 > n3 {}'.format(maior))
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
        print('Menor: n1 < n3 {}'.format(menor))
    elif n1 > n3:
        menor = n3
        print('Menor: n1 > n3 {}'.format(menor))
elif n1 > n2:
    if n2 <= n3:
        menor = n2
        print('Maior n2 < n3: {}'.format(menor))
    elif n3 <= n2:
        menor = n3
        print('Maior n3 < n2: {}'.format(menor ))