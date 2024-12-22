"""
Faça um programa que leia uma frase e mostre:
- Quantas vezes aparece a letra 'A'
- Em que posição ela aparece pela primeira vez
- Em que posição ela aparece pela ultima vez
"""

frase: str = input("frase: ")
frase = frase.upper()

print(f"'A' aparece {frase.count('A')}\n"
      f"'A' aparece pela primeira vez no indice {frase.find('A')}\n"
      f"'A' aparece pela última vez no indice {frase.rfind('A')}")