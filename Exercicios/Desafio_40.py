"""
Peça duas notas de um aluno e calcule a média
- Abaixo de 5.0 -> reprovado
- Entre 5.0 e 6.9 -> Recuperação
- 7.0+ -> Aprovado
"""

lista_notas: list = []

for i in range(2):
    nota: float = float(input(f"Nota {i+1}: "))
    lista_notas.append(nota)

aprovado: bool = sum(lista_notas) / 2 >= 7.0
recuperacao: bool = sum(lista_notas) / 2 >= 5.0 and sum(lista_notas) / 2 <= 6.9

if aprovado:
    print(f"Média {sum(lista_notas) / 2}: APROVADO")
elif recuperacao:
    print(f"Média {sum(lista_notas) / 2}: RECUPERAÇÃO")
else:
    print(f"Média {sum(lista_notas) / 2}: REPROVADO")