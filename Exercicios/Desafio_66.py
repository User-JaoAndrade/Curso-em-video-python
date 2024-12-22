"""
Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""

number_count: int = 0
sum_number: int = 0

while True:
    number: int = int(input("Digite um número (999 para parar): "))
    if number == 999:
        break
    sum_number+=number
    number_count+=1

print(f"Foram digitados {number_count} números e todos somados foram {sum_number}")