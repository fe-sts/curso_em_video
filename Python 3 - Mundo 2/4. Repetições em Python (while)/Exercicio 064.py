#Crie um programa que leia varios numeros inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar 999, que é a condição de parada.
#No final mostre quantos numeros foram digitados e qual a soma entre eles (desconsiderando o flag "999")

num = 0
qntdade = 0
soma = 0

while num != 999:
    num  = int(input("Digite um numero: "))
    soma += num
    qntdade += 1

print(f"Foram digitados {qntdade-1} numeros\nA soma deles é {soma-999}")
