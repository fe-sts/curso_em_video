'''
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um 
terreno retangular (largura e comprimento) e mostre a área do terreno.

'''
largura = 0
comprimento = 0


def area(largura, comprimento):
    area_c = largura * comprimento
    return area_c

print(' CONTROLE DE TERRENOS')
print('-'*20)
largura = float(input("Digite a largura: ").strip())
comprimento = float(input("Digite o comprimento: ").strip())

area_calc = area(largura, comprimento)
print(f'A área calculada é de: {area_calc}m².')
