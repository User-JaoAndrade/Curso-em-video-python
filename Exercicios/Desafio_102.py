"""
Crie um programa que tenha uma função chamada fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""
def fatorial(n, boolean):
    number: int = 1

    while n != 0:
        number *= n
        if boolean:
            print(f"{n}", end=" x " if n > 1 else " = ")
        n -= 1
    print(number)

if __name__ == '__main__':
    numero: int = int(input("Numero: "))

    fatorial(numero, True)