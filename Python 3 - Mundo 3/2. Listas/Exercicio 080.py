'''
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em 
uma lista, já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela.
'''
lista = []
for cont in range(0, 5):
    n = int(input("Digite um valor: "))
    if cont == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('Os valores digitados foram: {}'.format(lista))