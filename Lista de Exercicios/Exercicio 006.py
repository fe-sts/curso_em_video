#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

n1 = int(input('Digite um numero: '))

print('Para o numero {} \n Seu dobro é: {} \n Seu triplo é: {} \n Sua raiz quadrada é {:.2f}'.format(n1, n1 * 2, n1 * 3, n1 ** (1/2)))

print('Raiz quadrada de outra forma {:.2f}'.format(pow(n1, (1/2))))