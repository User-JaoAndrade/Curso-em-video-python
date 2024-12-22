"""
Verificando se uma string é um palindromo
"""

palavra: str = input("Palavra: ")

if palavra.upper() == ''.join(reversed(palavra)).upper():
    print("É UM PALINDROMO\n")
else:
    print("NÃO É UM PALINDROMO\n")