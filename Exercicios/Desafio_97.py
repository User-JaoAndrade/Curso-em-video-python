"""
Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Exemplo:
Se o texto passado for "Olá, Mundo!", a saída deve ser:

~~~~~~~~~~~~~~~
  Olá, Mundo!  
~~~~~~~~~~~~~~~
"""
def escreva(msg) -> str:
    tamanho: int = len(msg) + 6
    print("~" * tamanho)
    print(f'   {msg}')
    print("~" * tamanho)

if __name__ == '__main__':
    mensagem: str = input("Frase: ")
    escreva(mensagem)