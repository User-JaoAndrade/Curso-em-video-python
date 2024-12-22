"""
"Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

A média de idade do grupo.
O nome do homem mais velho.
Quantas mulheres têm menos de 20 anos.

"""

idades_somadas: int = 0
numero_max_pessoas: int = 0
idade_homem_mais_velho: float = float('-inf')
nome_homem_mais_velho: str = ''
mulheres_menos_de_vinte: int = 0

for i in range(1, 5):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [H]omem [M]ulher: ").upper()

    if (sexo == 'H') and (idade > idade_homem_mais_velho):
        nome_homem_mais_velho = nome
        idade_homem_mais_velho = idade

    elif (sexo == 'M') and (idade < 20):
        mulheres_menos_de_vinte += 1

    idades_somadas += idade
    numero_max_pessoas += 1
    

print(f"\nA Média de idade do grupo é de {idades_somadas / numero_max_pessoas}\n"
      f"O homem mais velho se chama {nome_homem_mais_velho}, ele tem {idade_homem_mais_velho} anos\n"
      f"O grupo tem {mulheres_menos_de_vinte} mulheres com menos de 20 anos")