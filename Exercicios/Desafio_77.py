"""
Faça um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

lista_de_palavras: tuple = ("Sonic", "Tails", "knuckles", "Amy", "Silver", "Blaze", "Shadow", "Rouge")
vogais: tuple = ("aeiou")

for _, palavra in enumerate(lista_de_palavras):
    print(f"{palavra.upper()} possui as seguintes vogais: ", end='')
    
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra,end='')
    print("")