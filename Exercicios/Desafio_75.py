"""
O enunciado do **Desafio 75** do curso de Python do Curso em Vídeo é o seguinte:

---

**Desafio 75**  
Crie um programa que leia **quatro valores pelo teclado** e guarde-os em uma **tupla**. No final, mostre:

1. Quantas vezes apareceu o valor 9.  
2. Em que posição foi digitado o primeiro valor 3.  
3. Quais foram os números pares.
"""

tupla: list = []
valor_nove: int = 0
pares: list = []

for i in range(4):
    valor = int(input(f"Informe o {i+1}º número: "))
    if valor == 9:
        valor_nove+=1
    if valor % 2 == 0:
        pares.append(valor)

    tupla.append(valor)

tupla = tuple(tupla)

print(f"O valor 9 apareceu {valor_nove} vezes\n"
      f"O primeiro valor 3 está na posição {tupla.index(3)}\n"
      f"Os números pares informados foram", *pares)