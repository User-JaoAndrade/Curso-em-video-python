"""
Leia a velocidade de um carro. Se ele ultrapassar 80Km/h mostre uma mensagem que ele foi multado
A multa será de R$7,00 reais para cada KM acima do limite
"""

speed: float = float(input("O Radar detectou um carro à: "))

if speed <= 80:
    print("De boa chefe (y)")
else: 
    print(f"Está {speed - 80}km acima do limite\n"
          f"Multa de R${7 * (speed - 80):.2f}")