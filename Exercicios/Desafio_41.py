"""
lEIA O ANO DE NASCIMENTO DE UMA ATLETA e mostre sua categoria de acordo com a idade
- até 9 anos-> MIRIM
- até 14 anos-> INFANTIL
- até 19 anos-> JUNIOR
- até 25 anos-> SENIOR
- ACIMA-> MASTER
"""

from datetime import date
from rich.console import Console

collor = Console()
ano_atual = date.today().year
ano_nascimento: int = int(input("Ano de nascimento: "))
idade: int = ano_atual - ano_nascimento

mirim: bool = idade <= 9
infantil: bool = idade > 9 and idade <= 14
junior: bool = idade > 14 and idade <= 19
senior: bool = idade > 19 and idade <= 25

if mirim:
    collor.print(f"Voce tem {idade} anos! CATEGORIA: [cyan]MIRIM[/cyan]")
elif infantil:
    collor.print(f"Voce tem {idade} anos! CATEGORIA: [green]INFANTIL[/green]")
elif junior:
    collor.print(f"Voce tem {idade} anos! CATEGORIA: [purple]JÚNIOR[/purple]")
elif senior:
    print(f"Voce tem {idade} anos! CATEGORIA: SENIOR")
else:
    collor.print(f"Voce tem {idade} anos! CATEGORIA: [red]MASTER[/red]")