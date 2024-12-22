"""
Crie um programa que tenha um menu de opções para o usuário:

[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos números
[5] Sair

O programa deverá repetir o menu até que o usuário escolha a opção de sair. 
Cada vez que o usuário escolher uma opção, o programa deve realizar a operação correspondente (como soma, multiplicação, etc.). 
O programa também deve permitir que o usuário insira dois números e, conforme a escolha, realize a operação desejada
"""
def soma(num1, num2) -> None:
    print(f"\n{num1} + {num2} = {num1 + num2}\n")

def multiplicacao(num1, num2) -> None:
    print(f"\n{num1} * {num2} = {num1 * num2}\n")

def maior(num1, num2) -> None:
    if not num1 == num2:
        print(f"\nNúmero {num1} é maior\n" if num1 > num2 else f"\nNúmero {num2} é maior\n")
    else:
        print("\nOS NÚMEROS SÃO IGUAIS\n")

def main() -> None:
    numero_1: int = int(input("Número 1: "))
    numero_2: int = int(input("Número 2: "))
    opcao: str = None

    while opcao != 5:
        opcao = input(">>> MENU <<<\n"
                      "[1] Soma\n"
                      "[2] Multiplicação\n"
                      "[3] Maior\n"
                      "[4] Novos Números\n"
                      "[5] Sair\n"
                      "-> ")
        
        match opcao:
            case '1':
                soma(numero_1, numero_2)
            case '2':
                multiplicacao(numero_1, numero_2)
            case '3':
                maior(numero_1, numero_2)
            case '4':
                main()
            case '5':
                print("Saindo...")
                exit()
            case _:
                pass

if __name__ == "__main__":
    main()