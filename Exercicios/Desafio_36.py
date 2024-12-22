"""
Aprove o empréstimo bancário para compra de uma casa. Pergunte o VALOR DA CASA, o salário do comprador 
e em QUANTOS ANOS vai pagar
a prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado
"""
from rich.console import Console

collor = Console()
salario: float = float(input("Salário: "))
valor_casa: float = float(input("Valor da casa: "))
anos_para_pagar: int = int(input("Quantos anos vai pagar: "))

prestacao = valor_casa / (12 * anos_para_pagar)

print(f"Para pagar uma casa de R${valor_casa:.2f} em {anos_para_pagar} anos\na prestação será de R${prestacao}")

trinta_porcento_salario = salario * 30 / 100

if prestacao <= trinta_porcento_salario:
    collor.print("[bold green]EMPRÉSTIMO APROVADO[/bold green]")
else:
    collor.print("[bold red]EMPRÉSTIMO DESAPROVADO[/bold red]")