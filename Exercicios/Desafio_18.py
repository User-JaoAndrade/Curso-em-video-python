"""
Leia o ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente 
"""

import math

angulo: float = float(input("Informe o ângulo: "))
angulo_radiano = math.radians(angulo)

print(f"Seno de {angulo} graus -> {math.sin(angulo_radiano):.2f}\n"
      f"Cosseno de {angulo} graus -> {math.cos(angulo_radiano):.2f}\n"
      f"Tangente de {angulo} graus -> {math.tan(angulo_radiano):.2f}")