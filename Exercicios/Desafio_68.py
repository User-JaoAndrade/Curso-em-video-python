"""
Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

import random

def impar_ou_par(m, u) -> bool:
    if (m + u) % 2 == 0:
        return True
    else:
        return False


# INICIO DO PROGRAMA
user_wins: int = 0
while True:
    machine_number: int = random.randint(1, 10)
    user_par_ou_impar: str = input("[P]ar\n[I]mpar\n-> ")
    user_number: int = int(input("\nInforme um número de 1 ate 10: "))
    
    if user_par_ou_impar.upper() == 'P':
        if impar_ou_par(machine_number, user_number):
            print("\n>>> PAR <<<\n")
            user_wins += 1
        else:
            break

    elif user_par_ou_impar.upper() == 'I':
        if not impar_ou_par(machine_number, user_number):
            print("\n>>> IMPAR <<<\n")
            user_wins += 1
        else: 
            break
        
    else:
        print("\ninforme P ou I\n")
        continue


print("VOCÊ PERDEU")
print(f"\nUsuário venceu {user_wins} vez" if user_wins < 2 else f"\nUsuário venceu {user_wins} vezes")
            
