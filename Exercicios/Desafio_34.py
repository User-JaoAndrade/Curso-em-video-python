"""
Informe o salário de um funcionário e calcule o valor do seu aumento.
Para saários superiores a 1250,00 calcula-se um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%
"""
salario: float = float(input("Salário: "))

if salario > 1250.00:
    print(f"Seu salário atual é de R${salario + ((salario * 10) / 100):.2f}")
else:
    print(f"Seu salaário atual é de R${salario + ((salario * 15) / 100):.2f}")