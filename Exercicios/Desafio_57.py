"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto
"""

sex: str = None

while sex != 'M' and sex != 'F':
    sex = input("Informe seu sexo: ").upper()

print(f"Sexo {sex} cadastrado com sucesso")