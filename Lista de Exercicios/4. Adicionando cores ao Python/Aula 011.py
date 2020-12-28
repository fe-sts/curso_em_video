#TESTES

#\033[0;30;41m
#\033[4;33;44m
#\033[1;35;43m
#\033[30;42m
#\033[m #CONFIGURAÇÃO PADRÃO
#\033[7;30m

print('\033[1;30;41mOlá, Mundão! \033[m')
print('\033[4;33;44mOlá, Mundão!')
print('\033[1;35;43mOlá, Mundão!')
print('\033[30;42mOlá, Mundão!')
print('\033[mOlá, Mundão!') #CONFIGURAÇÃO PADRÃO
print('\033[7;30mOlá, Mundão!\033[m')

#UTILIZANDO CORES PELO .format
nome = "Felipe"
cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31;40m',
         'azul' : '\033[1;34m'}

print('Olá, meu nome é: {}{}{}'.format(cores['vermelho'], nome, cores['limpa']))
print('Olá, meu nome é: {}{}{}'.format(cores['azul'], nome, cores['limpa']))
