#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
import math
angulo = float(input('Digite o ângulo para saber os valores de seu seno e cosseno: '))

seno = math.sin(angulo)
cos = math.cos(angulo)
print('Para o ângulo de {}º, o seno é {} e o cosseno é {}'.format(angulo, seno, cos))