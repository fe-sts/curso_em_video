#Crie um programa que leia uma frase
#1. Quantas vezes aparece a Letra A
#2. Em que posição ela aparece a primeira vez
#3. Em que posição ela aparece a ultima vez

#1 Tentei trabalhar com Lista ==> estaá Errado
#frase = list(input('Digite uma frase: ').strip())
#frase_str = str(frase)
#frase_upper = frase_str.upper()
#print(type(frase_upper), frase_upper)
#print(frase_upper.count('A'))
#2
#print(frase_upper.find('L'))

#Outro jeito
frase2 = str(input('Digite uma frase: ')).upper().strip()
print('A Letra A aparece {} vezes na frase'.format(frase2.count('A')))
print('A primeira Letra A apareceu na posição {}'.format(frase2.find('A') + 1))
print('A ultima Letra A apareceu na posição {}'.format(frase2.rfind('A') + 1))