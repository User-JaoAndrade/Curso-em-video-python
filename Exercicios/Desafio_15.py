"""
Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado
"""

CAR_DAY: int = 60
KM_PRICE: float = 0.15

dias_de_aluguel: int = int(input("Por quantos dias alugou o carro?\n-> "))
km_driven: float = float(input("Quantos kilômetros rodados?\n-> "))

print(f"Você precisa pagar R${(CAR_DAY * dias_de_aluguel) + (KM_PRICE * km_driven):.2f}")