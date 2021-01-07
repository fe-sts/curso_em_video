'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
'''

frase = str(input('Digite uma frase para saber se é palíndromo: ').strip().upper())
frase_sem_espaco = ''.join(frase.split())
reversa = frase_sem_espaco[::-1]
print('\033[1:31:40m A palavra invertida fica:\033[m \n{} '.format(reversa))
if frase_sem_espaco == reversa:
    print('A frase é um palíndromo!')
else:
    print('A frase Não é um palíndromo!')
