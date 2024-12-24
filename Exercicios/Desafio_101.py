"""
O Desafio 101 do Curso em Vídeo consiste em criar um programa que tenha uma função chamada voto() 
e que receba como parâmetro o ano de nascimento de uma pessoa. 
Essa função deve retornar um valor indicando se a pessoa não vota, 
se o voto é opcional ou se o voto é obrigatório, conforme a idade calculada.

As regras são baseadas na legislação eleitoral brasileira:

Menores de 16 anos: Não votam.
Entre 16 e 17 anos ou acima de 65 anos: Voto opcional.
Entre 18 e 65 anos: Voto obrigatório.
"""
from datetime import datetime

def voto(data):
    idade: int = datetime.today().year - data
    print(idade)
    if idade < 16:
        return 'Não vota'
    elif (idade == 16 or idade == 17) or idade > 65:
        return 'Voto opcional'
    else:
        return 'Voto Obrigatório'
    
if __name__ == '__main__':
    data_de_nascimento: int = int(input("Informe sua data de nascimento: "))
    print(voto(data_de_nascimento))