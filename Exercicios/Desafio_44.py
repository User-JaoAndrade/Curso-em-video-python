"""
Crie um programa que leia o valor de uma compra e calcule o valor a ser pago de acordo com a forma de pagamento escolhida:

À vista (dinheiro ou cheque): 10% de desconto.
À vista no cartão: 5% de desconto.
Em até 2 vezes no cartão: preço normal (sem juros).
3 vezes ou mais no cartão: 20% de juros.

O programa deve mostrar o valor final a ser pago, com base na opção de pagamento escolhida, 
e também o valor das parcelas caso o pagamento seja parcelado.
"""

opcao = None
while opcao != '5':
    valor_compra: float = float(input("Valor da compra: "))

    opcao = input("\nForma de Pagamento\n\n"
                  "[1] À VISTA (dinheiro ou cheque) -> 10% de desconto\n"
                  "[2] À VISTA (CARTÃO) -> 5% de desconto\n"
                  "[3] 2 VEZES -> Sem Juros\n"
                  "[4] 3+ VEZES -> 20% de Juros\n"
                  "[5] Sair\n-> ")

    match opcao:
        case '1':
            print(f"\n10% de desconto: R${valor_compra - (valor_compra * 10 / 100):.2f}")
        case '2':
            print(f"\n05% de desconto: R${valor_compra - (valor_compra * 5 / 100):.2f}")
        case '3':
            print(f"\nSem Juros: R${valor_compra:.2f} cada parcela terá um valor de R${valor_compra / 2:.2f}")
        case '4':
            parcelas: int = int(input("\n\nParcelas: "))
            print(f"20% de Juros: R${valor_compra + (valor_compra * 20 / 100):.2f} cada parcela terá um valor de R${(valor_compra + (valor_compra * 20 / 100)) / parcelas:.2f}")
        case '5':
            exit()
        case _:
            continue