"""
Calcule o IMC de uma pessoa
- abaixo de 18.5-> abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 ate 30: sobrepeso
- 30 até 40: Obesidade
- Acima de 40: obesidade morbida
"""

peso: float = float(input("Peso: "))
altura: float = float(input("Altura: "))

imc: float = peso / pow(altura, 2)

abaixo_do_peso: bool = imc < 18.5
peso_ideal: bool = 18.5 <= imc < 25
sobrepeso: bool = 25 <= imc < 30
obesidade: bool = 30 <= imc < 40

print(f"Seu IMC é {imc:.2f} você está ", end='')
if abaixo_do_peso:
    print("Abaixo do peso")
elif peso_ideal:
    print("com o peso ideal")
elif sobrepeso:
    print("com sobrepeso")
elif obesidade:
    print("com obesidade")
else:
    print("com Obesidade Mórbida")