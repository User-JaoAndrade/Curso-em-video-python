"""
O enunciado do Desafio 45 do curso em vídeo de Python propõe a criação de um programa que simula o jogo Pedra, Papel e Tesoura (Jokenpô)
entre o usuário e o computador. O computador deve fazer uma escolha aleatória e, em seguida,
o programa deve exibir quem venceu o jogo com base nas regras tradicionais:

Pedra vence Tesoura
Tesoura vence Papel
Papel vence Pedra

Você deve criar um sistema onde o usuário escolhe sua jogada e o computador escolhe aleatoriamente.
O programa então mostra as escolhas de ambos e declara o vencedor​
"""

import random
"""
1 - pedra
2 - papel
3 - tesoura
"""
tie_score: int = 0
machine_wins_score: int = 0
player_wins_score: int = 0
opcao: str = None

while opcao != '4':
    machine_choice: int = random.randint(1, 3)

    print(f"Player Wins: {player_wins_score}\n"
          f"Machine Wins: {machine_wins_score}\n"
          f"TIE: {tie_score}\n")
    
    opcao = input("PEDRA PAPEL TESOURA\n"
                  "[1] Pedra\n"
                  "[2] Papel\n"
                  "[3] Tesoura\n"
                  "[4] Sair\n-> ")

    # Condições
    player_rock_wins: bool = opcao == '1' and machine_choice == 3
    player_scissors_wins: bool = opcao == '3' and machine_choice == 2
    player_paper_wins: bool = opcao == '2' and machine_choice == 1

    machine_rock_wins: bool = machine_choice == 1 and opcao == '3'
    machine_scissors_wins: bool = machine_choice == 3 and opcao == '2'
    machine_paper_wins: bool = machine_choice == 2 and opcao == '1'

    print("\n\n>>>> RESULTADO <<<<")
    # Verificações
    if player_rock_wins:
        print("Pedra (user) amassa tesoura (machine)\n")
        player_wins_score += 1
    elif machine_rock_wins:
        print("Pedra (Machine) amassa tesoura (user)\n")
        machine_wins_score += 1

    elif player_scissors_wins:
        print("Tesoura (user) corta papel (machine)\n")
        player_wins_score += 1
    elif machine_scissors_wins:
        print("Tesoura (machine) corta papel (user)\n")
        machine_wins_score += 1

    elif player_paper_wins:
        print("Papel (user) engole pedra (machine)\n")
        player_wins_score += 1
    elif machine_paper_wins:
        print("Papel (machine) engole pedra (user)\n")
        machine_wins_score += 1

    else:
        print("Empate\n")
        tie_score += 1
    