"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele 
AINDA vai se alistar
É HORA de se alista
JÁ PASSOU DA HORA de se alistar
"""
from datetime import date

ano_atual = date.today().year
ano_nascimento: int = int(input("Ano de nascimento: "))

if ano_atual - ano_nascimento == 18:
    print("É HORA DE SE ALISTAR PAIZAO")
elif ano_atual - ano_nascimento > 18:
    print("JÁ PASSOU DA HORA DE SE ALISTAR")
else: 
    print("AINDA VAI SE ALISTAR")