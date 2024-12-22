"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, 
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o 
programa vai informar quantas cédulas de cada valor serão entregues.

Observações:
Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
def calculando_cedulas(n):
    global valor
    contador: int = 0

    while valor != 0:
        aux_valor = valor
        valor-=n

        if valor < 0:
            valor = aux_valor
            break

        contador += 1

    return contador


valor: int = int(input("Valor para ser trocado: "))
cedulas_50 = calculando_cedulas(50)
print(f"{cedulas_50} cedulas de 50")

cedulas_20 = calculando_cedulas(20)
print(f"{cedulas_20} cedulas de 20")

cedulas_10 = calculando_cedulas(10)
print(f"{cedulas_10} cedulas de 10")

cedulas_5 = calculando_cedulas(5)
print(f"{cedulas_5} cedulas de 5")

cedulas_1 = calculando_cedulas(1)
print(f"{cedulas_1} cedulas de 1")