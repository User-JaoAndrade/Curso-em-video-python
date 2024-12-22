"""
Faça um programa que leia um número inteiro e veja se ele é primo ou não
"""
from rich.console import Console

collor = Console()
numero: int = int(input("Número: "))
divisores: int = 0

for i in range(1, numero + 1, 1):
    if numero % i != 0:
        collor.print(f"[bold red]{i}[/bold red]", end=' ')
    else:
        print(f"{i}", end=' ')
        divisores += 1

if divisores == 2:
    print("\nÉ UM NÚMERO PRIMO")
else:
    print("\nNÃO É UM NÚMERO PRIMO")