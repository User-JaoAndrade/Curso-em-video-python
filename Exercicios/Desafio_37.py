"""
Faça um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
"""
opcao: str = None

while opcao != '4':
    decimal: int = int(input("Número Decimal: "))
    opcao = input("\n[1] Binario\n"
                      "[2] Octadecimal\n"
                      "[3] Hexadecimal\n"
                      "[4] Exit\n-> ")
    
    match opcao:
        case '1':
            print(f"\nBinario de {decimal} é {bin(decimal)}") # bin(decimal)[2:] para retornar sem o 0b
        case '2':
            print(f"\nOctal de {decimal} é {oct(decimal)}") # oct(decimal)[2:] para retornar sem o 0o
        case '3':
            print(f"\nHexa de {decimal} é {hex(decimal)}") # hex(decimal)[2:] para retornar sem o 0x
        case _:
            exit()
