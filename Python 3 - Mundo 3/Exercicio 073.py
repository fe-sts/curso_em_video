'''
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time do Cuiabá.
'''

times = (
"Bahia"	,
"Red Bull Bragantino"	,
"Ceará"	,
"Fortaleza"	,
"Athletico-PR"	,
"Atlético-GO"	,
"Flamengo"	,
"Cuiabá"	,
"Internacional"	,
"Juventude"	,
"Sport"	,
"Fluminense"	,
"São Paulo"	,
"Grêmio"	,
"Atlético-MG"	,
"América-MG"	,
"Corinthians"	,
"Palmeiras"	,
"Chapecoense"	,
"Santos")
print("=-="*15)
print("Os 5 primeiros colocados são: {}".format(times[0:5]))
print("=-="*15)
print("Os 4 ultimos colocados são: {} ".format(times[-4:]))
print("=-="*15)
print("Times em ordem alfabética: {}".format(sorted(times)))
print("=-="*15)
print("A posição do Time Cuiabá é: {}a posição.".format(times.index("Cuiabá")+1))
