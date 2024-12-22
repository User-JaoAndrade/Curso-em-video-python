"""
Crie um programa que leia a posição de 20 times no Campeonato Brasileiro e os armazene em uma tupla. Depois, mostre:

Os 5 primeiros times da tabela.
Os últimos 4 times da tabela.
Os times em ordem alfabética.
Em que posição está o time da Chapecoense.
"""

times = (
    "Flamengo",
    "Palmeiras",
    "Atlético-MG",
    "Corinthians",
    "São Paulo",
    "Santos",
    "Internacional",
    "Grêmio",
    "Fluminense",
    "Botafogo",
    "Athletico-PR",
    "Cruzeiro",
    "Bahia",
    "Fortaleza",
    "Ceará",
    "Vasco da Gama",
    "Sport",
    "Goiás",
    "Coritiba",
    "Chapecoense"
)

print(f"Os 5 primeiros times da tabela são: {times[:5]}")
print(f"Os 5 últimos times são: {times[15:]}")
print(f"Os times em ordem alfabética: {sorted(times)}")
print(f"A Chapecoense está na posição: ", end='')
for i, j in enumerate(times):
    if j == 'Chapecoense':
        print(i + 1)
