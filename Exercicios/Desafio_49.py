"""
    peça ao usuario um número e imprima na tela a tabuada desse numero
"""

number: int = int(input("Deseja ver qual tabuada?\n-> "))

for i in range(1, 11):
    print(f"{i:2} x {number} = {number * i}")