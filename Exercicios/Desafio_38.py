"""
Escreva um programa que leia 2 números inteiros e compare-os
- O primeiro valor é maior
- O segundo valor é maior
- Iguais
"""

number_one: int = int(input("Número 1: "))
number_two: int = int(input("Número 2: "))

number_one_higher: bool = number_one > number_two
number_one_not_highter_then_two_and_number_two_not_highter_then_number_one: bool = number_one == number_two

if number_one_higher:
    print(f"Número um é maior")
elif number_one_not_highter_then_two_and_number_two_not_highter_then_number_one:
    print(f"{number_one} e {number_two} são iguais")
else:
    print(f"Número dois é maior")