from rich.console import Console
from menus.opcoes_menu import cadastrar, lista_cadastradas, limpar_terminal
    
def menu():
    collor = Console()
    opcao: str = ''

    while opcao != '3':
        limpar_terminal()
        print("-" * 50)
        print("MAIN MENU".center(50))
        print("-" * 50)
        collor.print("[bold blue]1 - Lista de Cadastros[/bold blue]\n"
                    "[bold blue]2 - Cadastrar[/bold blue]\n"
                    "[red]3 - SAIR[/red]\n-> ",end='')
        opcao = input().strip()

        match opcao:
            case '1':
                lista_cadastradas()
            case '2':
                cadastrar()
            case '3':
                exit()
            case _:
                pass