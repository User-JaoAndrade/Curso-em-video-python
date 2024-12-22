"""
Melhore o desafio 51 vendo se o user que ver mais termos, o programa encerra quando o usuario colocar 0
"""

primeiro_termo: int = int(input("Primeiro termo: "))
razao: int = int(input("Razão: "))
termo = 0
count = 0
saltos = None

for _ in range(1, 11):
    print(termo, ' -> ', end='')
    termo+=razao
    count += 1
    
print("PAUSE")

while True:
    saltos = int(input("Quantos termos deseja ver a mais?\n-> "))

    if saltos == 0:
        break
    else:
        verificador = 1
        while verificador <= saltos:
            print(termo," -> ", end='')
            termo += razao
            verificador += 1
            count+=1
        else:
            print("PAUSE")

print(f"\nprogressão finalizada com {count} termos")