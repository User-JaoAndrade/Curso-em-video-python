"""
Crie um programa que leia nome e duas notas de vário alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contando a média de cada um e permita que o usuário possa 
mostrar as notas de cada aluno individualmente
"""

lista_de_alunos: list = []
opcao: str = ''

while opcao.lower() != 's':
    nome: str = input("Nome: ")
    nota1: float = float(input("Nota 1: "))
    nota2: float = float(input("Nota 2: "))
    lista_de_alunos.append([nome, nota1, nota2, (nota1 + nota2) / 2])

    opcao = input("\nDeseja informar outro aluno? [S]im\n-> ")

for indice, alunos in enumerate(lista_de_alunos):
    print(f"{indice} | Aluno: {alunos[0]} | Média: {alunos[3]}")
