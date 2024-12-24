"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado
"""
import random
from operator import itemgetter

jogadores: dict = {'jogador 1': None, 'jogador 2': None, 'jogador 3': None, 'jogador 4': None}

for nome in jogadores:
    jogadores[nome] = random.randint(1,6)
    print(f"{nome} tirou {jogadores[nome]} no dado")

classificacao = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
classificacao = dict(classificacao)

posicao: int = 1
for nome in classificacao.keys():
    print(f"{posicao} Lugar: {nome}")
    posicao += 1