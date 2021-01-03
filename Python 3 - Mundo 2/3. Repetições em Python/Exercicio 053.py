'''
Desenvolva um programa que leia o 1o termo
'''

palavra = str(input('Digite uma frase para saber se é palíndromo: ').strip())
pal_sem_espaco = ''.join(palavra.split())
reversa = pal_sem_espaco[::-1]
print('\033[1:31:40m A palavra invertida fica:\033[m \n{} '.format(reversa))
if pal_sem_espaco == reversa:
    print('A frase é um palíndromo')
else:
    print('A frase Não é um palíndromo!')
