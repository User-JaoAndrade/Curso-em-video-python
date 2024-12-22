"""
Faça o programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pinta-la.
Sabendo que cada litro de tinta, pinta uma área de 2m^2
"""

height: float = float(input("Informe a altura da parede em metros: "))
width: float = float(input("Informe a largura da parede em metros: "))
area: float = height * width

print(f"\nA parede possui uma área de {area:.2f}m quadrados\n"
      f"Será necessário {area / 2}L de tinta para pintar a parede")