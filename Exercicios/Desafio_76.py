"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços organizando os dados em forma tabular.
"""

tupla_precos: tuple = ('Banana', 50,
                       'Maça', 60,
                       'Chocolate', 100,
                       'Salgadin do China', 7.50 
                       )
for i in range(len(tupla_precos)):
    if i % 2 == 0:
        print(f'{tupla_precos[i]} = ', end='')
    else:
        print(f'R${tupla_precos[i]}')