#Leia o comprimento de 3 retas e descubra se podem formar um triângulo
#* o comprimento de uma reta não pode ser maior que a soma do comprimento das outras 2 retas!
print('=-='*20)
print('Analisador de Triângulos')
print('=-='*20)
r1 = float(input('Entre com o comprimento da reta 1: '))
r2 = float(input('Entre com o comprimento da reta 2: '))
r3 = float(input('Entre com o comprimento da reta 3: '))


if (r1 + r2) > r3 or (r1 + r3) > r2 or r2 + r3 > r1:
    print('Sim! É possível formar um triângulo com essas retas!')
else:
    print('Não é possível formar um triângulo com essas retas!')

#OUTRO JEITO:
if r1 < (r2 + r3) or r2 < (r1 + r3) or r3 < (r1 + r2):
    print('Ok, é possivel formar um triângulo!')
else:
    print('Não é possível formar um triângulo com essas retas!')
