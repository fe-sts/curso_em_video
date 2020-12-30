'''
Desenvolva uma lógica que leia o peso e altura de uma pessoa.
Calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso Ideal
- 25 a 30: Sobrepeso
- 30 a 40: Obesidade
- Acima de 40: Obesidade mórbida

 IMC = peso/ (altura x altura)
'''

peso = float(input('Digite seu peso: ').strip())
altura = float(input('Digite sua altura: ').strip())
imc = peso / (altura**2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc >=18.5 and imc <= 25:
    print('Peso ideal')
elif imc > 25 and imc < 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')