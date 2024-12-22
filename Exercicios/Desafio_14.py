"""
Escreva um programa que converta uma temperatura digitada em C e converta para F
"""

temperature: float = float(input("Informe uma temperatura em Celcius: "))
print(f"{temperature}C é {temperature * 1.8 + 32}F")