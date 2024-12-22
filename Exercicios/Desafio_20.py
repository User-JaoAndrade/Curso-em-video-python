"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
"""

import random

list_students: list = []
for i in range(4):
    student: str = input(f"Aluno {i+1}: ")
    list_students.append(student)

random.shuffle(list_students)
print(*list_students)