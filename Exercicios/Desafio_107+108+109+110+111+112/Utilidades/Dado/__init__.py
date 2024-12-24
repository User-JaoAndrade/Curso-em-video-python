def leiaDinheiro(msg):
    dinheiro = input(msg).replace(',', '.')
    if dinheiro.isalpha() or dinheiro == '' or ' ' in dinheiro:
        print("VALOR INVÁLIDO")
        exit()
    else:
        dinheiro = dinheiro.replace(',', '.')
        return float(dinheiro)