"""
Refaça o desafio 51 usando while
"""

primeiro_termo: int = int(input("Primeiro termo: "))
razao: int = int(input("Razão: "))

decimo_termo: int = primeiro_termo + (10 - 1) * razao
count = 1
while count <= 10:
    print(primeiro_termo, end=' ')
    primeiro_termo+=razao
    count+=1