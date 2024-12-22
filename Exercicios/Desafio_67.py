"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.
"""

while True:
    number: int = int(input("Deseja ver a tabuada de qual número: "))
    
    if number < 0:
        break

    print("-" * 20)
    for i in range(1, 11):
        print(f"{i:2} x {number} = {i * number}")
    print("-" * 20)
    