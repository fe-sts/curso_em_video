#Crie um programa que leia varios numeros inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar 999, que é a condição de parada.
#No final mostre quantos numeros foram digitados e qual a soma entre eles (desconsiderando o flag "999")
#Utilizar break

num = cont = 0
while True:
    num = int(input('Digite um numero (para parar: 999): '))
    if num == 999:
        print('Fim programa!')
        break
    cont += num
print(f'A soma dos valores digitados foi {cont}')