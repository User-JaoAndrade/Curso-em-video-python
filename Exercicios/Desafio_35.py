"""
Faça um programa que peça o comprimento de 3 retas e veja se é 
possivel formar um triângulo
"""

lado_A: int = int(input("Comprimento lado 1: "))
lado_B: int = int(input("Comprimento lado 2: "))
lado_C: int = int(input("Comprimento lado 3: "))

A_B_maior_que_C = lado_A + lado_B > lado_C
A_C_maior_que_B = lado_A + lado_C > lado_B
B_C_maior_que_A = lado_B + lado_C > lado_A

if A_B_maior_que_C and A_C_maior_que_B and B_C_maior_que_A:
    print("Pode formar um triângulo")
else:
    print("Não pode formar um triângulo")