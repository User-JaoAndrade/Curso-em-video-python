"""
Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deve perguntar se o usuário quer ou não continuar. No final, mostre:

Quantas pessoas têm mais de 18 anos.
Quantos homens foram cadastrados.
Quantas mulheres têm menos de 20 anos.
"""

maior_de_idade: int = 0
num_homens: int = 0
mulheres_menos_de_vinte: int = 0

while True:
    print("CADASTRO DE USUÁRIO\n")
    idade: int = int(input("IDADE: "))
    sexo: str = input("Sexo [F]eminino ou [M]asculino: ")

    if idade > 18:
        maior_de_idade += 1
    if sexo.upper() == 'M':
        num_homens += 1
    if (sexo.upper() == 'F') and (idade < 20):
        mulheres_menos_de_vinte += 1
    
    sexo = input("Deseja continuar?\n[S]im ou [N]ão\n-> ")
    if sexo.upper() == 'S':
        continue
    else: 
        break

print(f"{maior_de_idade} pessoas são maiores de idade\n"
      f"{num_homens} homens foram cadastrados\n"
      f"{mulheres_menos_de_vinte} mulheres com menos de 20 anos")