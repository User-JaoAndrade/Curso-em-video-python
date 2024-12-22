"""
O programa deve solicitar ao usuário que insira um número inteiro e, após cada entrada, perguntar se o usuário deseja continuar. 
Ele pode responder com "Sim" ou "Não".
O programa irá armazenar a soma de todos os números, contar a quantidade de números inseridos, 
e também identificar o maior e o menor número digitado.
Ao final, o programa exibe:

A quantidade de números digitados.
A soma de todos os números.
A média dos números.
O maior e o menor número fornecido.

"""

menor_numero = float('inf')
maior_numero = float('-inf')
opcao = None

numero = int(input("Informe um número: "))
soma = numero
numeros_digitados = 1

while opcao != 'n':
    opcao = input("Deseja continuar [s]im [n]ão\n-> ").lower()
    if opcao == 's':
        numero = int(input("informe um número: "))
        numeros_digitados+=1
        soma+=numero
    
        if numero < menor_numero:
            menor_numero = numero
        else:
            maior_numero = numero

    pass

print(f"Você digitou {numeros_digitados} números e a média foi {soma / numeros_digitados:.2f}\n"
      f"O maior valor foi {maior_numero} e o menor foi {menor_numero}")