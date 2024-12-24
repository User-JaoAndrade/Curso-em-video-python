"""
Faça um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tel
"""

aluno: dict = {
    'Nome': None,
    'Media': None,
    'Situacao': None
}

aluno['Nome'] = input("Nome do Aluno: ")
aluno['Media'] = float(input("Media do Aluno: "))

if aluno['Media'] >= 6:
    aluno['Situacao'] = 'Aprovado'
else: 
    aluno['Situacao'] = 'Reprovado'

print(f"\nAluno: {aluno['Nome']}\n"
      f"Media: {aluno['Media']}\n"
      f"Situação: {aluno['Situacao']}")