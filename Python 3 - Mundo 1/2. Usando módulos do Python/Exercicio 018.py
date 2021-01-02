#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
import math
angulo = float(input('Digite o ângulo para saber os valores de seu seno e cosseno: '))

seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('Para o ângulo de {}º, o seno é {:.3f}, o cosseno é {:.3f} e a tangente é {:.3f}'.format(angulo, seno, cos, tan))
