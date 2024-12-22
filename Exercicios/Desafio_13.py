"""
Faça um algoritmo que leia o salário de um funcionário e mostre seuy novo salário com 15% de aumento
"""

salary: float = float(input("Seu salário? R$"))
print(f"Seu novo salário é de R${salary + (salary * 15 / 100)}")