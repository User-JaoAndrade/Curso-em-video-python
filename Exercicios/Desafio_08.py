"""
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
"""

meters: float = float(input("Informe uma distância em metros: "))

print(f"{meters}m\n"
      f"{meters*100}cm\n"
      f"{meters*1000}mm")