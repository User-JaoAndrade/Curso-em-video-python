"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario
se por acaso o ctps for diferente de zero, o dicionario receberá tambem o ano de contratação e o salario.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
"""
from datetime import datetime

ano_atual = datetime.now().year

funcionario: dict = {
    "Nome": None,
    "Ano de Nascimento": None,
    "Idade": None,
    "Carteira de trabalho": None,
}


funcionario['Nome'] = input("Informe seu nome: ")
funcionario['Ano de Nascimento'] = int(input("Ano de Nascimento: "))
funcionario['Idade'] = ano_atual - funcionario['Ano de Nascimento']
funcionario['Carteira de trabalho'] = int(input("Carteira de Trabalho: "))

if funcionario['Carteira de trabalho'] == 0:
    funcionario['Carteira de trabalho'] = 'Sem carteira de trabalho'
    print(f"")
else: 
    funcionario['Ano de contratação'] = int(input("Informe o ano de contratação: "))
    funcionario['Salario'] = float(input("Informe seu salário: "))
    funcionario['Aposentadoria'] = funcionario['Ano de contratação'] + 35

print("*" * 30)

for key, values in funcionario.items():
    print(f"{key}: {values}")
