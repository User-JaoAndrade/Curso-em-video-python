"""
Faça um programa que tenha uma lista chamada numeros e duas funções chamadas
sorteio() e somaPar(). A primeira função vai sortear 5 números e vai coloca-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados
pela função anterior
"""
import random
import time

def somaPar(lista) -> int:
    soma: int = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            soma += lista[i]
    return soma

def sorteio() -> int:
    return random.randint(1, 6)

if __name__ == '__main__':
    numeros: list = []

    for _ in range(6):
        i: int = sorteio()
        time.sleep(0.5)
        print(f"{i} ", end='')
        numeros.append(i)
    
    print(f"\nSoma dos pares = {somaPar(numeros)}")