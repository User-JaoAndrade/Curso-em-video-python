"""
desenvolva um programa que leia vários números inteiros informados pelo usuário. 
O programa deve continuar recebendo números até que o valor 999 seja digitado, que serve como um sinal de parada. 
Quando o valor 999 for digitado, o programa deve exibir dois resultados:

A quantidade de números digitados (excluindo o 999).
A soma de todos os números informados, também desconsiderando o 999
"""

count = 0
soma = 0
while True:
    numero = int(input("Informe um número [999 pra parar]: "))
    if numero == 999:
        break
    count+=1
    soma+=numero

print(f"Você digitou {count} números e a soma entre eles foi de {soma}")