"""
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
de digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
def leiaFloat(m):
    try:
        numero: float = float(input("Numero de ponto flutuante: "))
    except:
        print("Informe um número de ponto flutuante")
        exit()
    return numero

def leiaInt(m):
    try:
        numero: int = int(input("Numero inteiro: "))
    except:
        print("Informe um número inteiro")
        exit()
    return numero

n = leiaInt("Digite um número inteiro: ")
print(f"Você digitou o número inteiro: {n}")

n = leiaFloat("Digite um número de ponto flutuante: ")
print(f"Você digitou o número de ponto flutuante: {n}")