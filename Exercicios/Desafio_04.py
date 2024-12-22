"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela
"""

user_info: str = input("Digite algo: ")
print("O tipo primitivo da sua variável é ", type(user_info))
print("\nSó tem números? ", user_info.isnumeric(),
      "\nSó tem letras? ", user_info.isalpha(),
      "\nÉ um espaço em branco? ", user_info.isspace(),
      "\nSó tem letras maiúsculas? ", user_info.isupper(),
      "\nSó tem letras minúsculas? ", user_info.islower())