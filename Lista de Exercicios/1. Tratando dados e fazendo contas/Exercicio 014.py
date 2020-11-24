#Converter graus celsius em farenheit e kelvin

celsius = float(input('Entre com a temperatura em graus Celsius (ºC): '))
farenheit = (((9 * celsius) / 5) + 32)
print('A temperatura de {0}ºC corresponde a {1} ºF'.format(celsius, farenheit))

kelvin = celsius + 273
print('A temperatura de {0}ºC corresponde a {1} ºK'.format(celsius, kelvin))
