def aumentar(price, aumento, format=True):
    coin = ((price * aumento) / 100) + price
    format_coin = moeda(coin)
    return format_coin if format else coin


def diminuir(price, diminuicao, format=True):
    coin = price - ((price * diminuicao) / 100)
    format_coin = moeda(coin)
    return format_coin if format else coin


def dobro(price, format=True):
    coin = price * 2
    format_coin = moeda(coin)
    return format_coin if format else coin

def moeda(price):
    return f'R${price:.2f}'.replace('.', ',')


def informacoes(price, aumento, diminuicao):
    str_coin: str = moeda(price)
    print(f"{str_coin} + {aumento}% = {aumentar(price, aumento)}")
    print(f"{str_coin} - {diminuicao}% = {diminuir(price, diminuicao)}")
    print(f"O Dobro de {str_coin} = {dobro(price)}")