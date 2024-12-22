"""
Melhore o jogo do DESAFIO 28 onde o computador vai 'pensar' em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
"""

import random

machine_num: int = random.randint(0, 10)
num_user: int = None
tentativas: int = 0

print(">>> ADVINHE A PALAVRA QUE ESTOU PENSANDO <<<")
while machine_num != num_user:
    tentativas += 1
    num_user = int(input(f"Tentativa {tentativas}: "))

print(f"\nVocê acertou com {tentativas} tentativas")