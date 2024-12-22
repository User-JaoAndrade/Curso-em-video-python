"""
Peça um ano e diga se ele é bissexto
"""

year: int = int(input("Ano: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("BISSEXTO")
else:
    print("NÃO É BISSEXTO")