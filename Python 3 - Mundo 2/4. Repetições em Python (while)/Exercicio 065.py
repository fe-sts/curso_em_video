#Crie um programa que leia varios numeros inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não Continuar a digitar.

num = []
continua = "S"
while continua in "Ss":
    num.append(int(input("Digite um numero: ")))
    continua = input("Deseja continuar? (S/N)")
    while continua not in "NnSs":
        print('Resposta errada. Digite S ou N') 
        continua = input("Deseja continuar? (S/N)")
print("A média entre todos os valores lidos é {}".format(sum(num)/len(num)))