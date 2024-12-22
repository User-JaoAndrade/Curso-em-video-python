"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome escolhido
"""

import random

list_students: list = []
for i in range(4):
    student: str = input(f"Aluno {i+1}: ")
    list_students.append(student)

print(f"{random.choice(list_students)} vai apagar o quadro")