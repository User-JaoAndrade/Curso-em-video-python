"""
Pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando 0.50 por km para viagens de até 200km
e 0.45 para viagens mais longas
"""

distance: float = float(input("Distância: "))

if distance < 0:
    exit()
elif distance <= 200:
    print(f"Passagem por R${0.50 * distance::.2f}")
else:
    print(f"Passagem por R${0.45 * distance:.2f}")