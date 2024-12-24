import pandas as pd
from time import sleep
import os

def limpar_terminal(): 
    os.system("cls" if os.name == "nt" else "clear")

def carregando_csv():
    try:
        # carrega o arquivo csv
        df = pd.read_csv("arquivos/cadastradas.csv")
    except FileNotFoundError:
        # Cria o arquivo caso ele não exista
        df = pd.DataFrame(columns=['Nome', 'Idade'])
        print("Banco de dados criado com sucesso")
        sleep(2)
        
    return df

def cadastrar():
    limpar_terminal()

    print('-' * 50)
    print("CADASTRAR".center(50))
    print('-' * 50)

    nome = input("Nome: ")

    while True:
        try:
            idade = int(input("Idade: "))
            break
        except ValueError:
            print("ATENÇÃO: Informe um número válido para a idade\n")
    
    # Adicionando o cadastro no arquivo CSV
    adicionando_no_csv(nome, idade)

def adicionando_no_csv(nome, idade):
    df = carregando_csv()

    # Adicionando um novo cadastro
    novo_cadastro = pd.DataFrame({'Nome': [nome], 'Idade': [idade]})
    df = pd.concat([df, novo_cadastro], ignore_index=True)
    
    # Salvando no arquivo csv
    df.to_csv("arquivos/cadastradas.csv", index=False)

    print("Cadastro realizado com sucesso!")
    sleep(2)

def lista_cadastradas():
    df = carregando_csv()
    limpar_terminal()

    print("-" * 50)
    print(df)
    print("-" * 50)
    input("\nAperte ENTER para continuar...")