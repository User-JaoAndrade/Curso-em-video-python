"""
O programa deve solicitar ao usuário o primeiro termo e a razão da progressão aritmética. 
Com esses dados, o programa precisa calcular e mostrar os 10 primeiros termos dessa progressão,
seguidos pela palavra "Fim". O cálculo da PA segue a fórmula: termo =  primeiro termo + (n - 1) x razão
"""

primeiro_termo: int = int(input("Primeiro termo: "))
razao: int = int(input("Razão: "))

decimo_termo: int = primeiro_termo + (10 - 1) * razao

for i in range(primeiro_termo, decimo_termo + razao, razao):
    print(i, end=' ')
print("FIM")