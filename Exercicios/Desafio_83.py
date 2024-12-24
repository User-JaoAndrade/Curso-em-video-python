"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu programa deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta
"""

expressao = str(input('Digite a expressão: '))
contador_parenteses: int = 0

for i in expressao:
    if i == '(':
        contador_parenteses += 1
    elif i == ')':
        contador_parenteses-=1

        if contador_parenteses < 0:
            break

print("Expressão Válida" if contador_parenteses == 0 else "Expressão Inválida")