"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:

O nome de um jogador;
Quantos gols ele marcou.
O programa deve ser capaz de mostrar a ficha do jogador, 
mesmo que algum dado não tenha sido informado corretamente.
"""

def ficha (nome, gols):
    return f'{nome} fez {gols} gols'

if __name__ == '__main__':
    nome: str = input("Informe o nome do jogador: ")
    gols: int = input("Informe a quantidade de gols: ")

    if gols.isdigit():
        gols = int(gols)
    else: 
        gols = 0
    
    if not nome:
        nome = '<desconhecido>'

    print(ficha(nome, gols))