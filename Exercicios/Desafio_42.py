"""
Refaça o desafio 35 dos triângulos acrescentando o tipo do triângulo
- Equilátero: TODOS OS LADOS SÃO IGUALS
- Isósceles: Dois lados são iguais
- Escaleno: TODOS os lados são diferentes
"""


def validacao_triangulo() -> bool:
    A_B_maior_que_C = lado_A + lado_B > lado_C
    A_C_maior_que_B = lado_A + lado_C > lado_B
    B_C_maior_que_A = lado_B + lado_C > lado_A

    if A_B_maior_que_C and A_C_maior_que_B and B_C_maior_que_A:
        return True
    else:
        print("Não pode formar um triângulo")
        exit()


# START
lado_A: int = int(input("Comprimento lado 1: "))
lado_B: int = int(input("Comprimento lado 2: "))
lado_C: int = int(input("Comprimento lado 3: "))

validacao_triangulo()

todos_os_lados_iguais: bool = lado_A == lado_B == lado_C
dois_lados_iguais: bool = (lado_A == lado_B) or (lado_A == lado_C) or (lado_B == lado_C)

print("Triângulo do tipo: ", end='')
if todos_os_lados_iguais:
    print("Equilátero")
elif dois_lados_iguais:
    print("Isósceles")
else: 
    print("Escaleno")