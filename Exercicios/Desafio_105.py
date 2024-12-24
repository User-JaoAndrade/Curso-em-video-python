"""
Faça um programa que tenha uma função chamada notas(), 
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

Quantidade de notas;
    A maior nota;
    A menor nota;
    A média da turma;
    A situação (opcional), que pode ser:
        "Boa" se a média for maior ou igual a 7;
        "Razoável" se a média for entre 5 e 7 (exclusivo);
        "Ruim" se a média for menor que 5
"""
def notas(*nota, situacao=False):
    """
    notas(notas(suporta varios valores), situacao(opcional))
    *nota: recebe vários valores para a tupla nota
    situacao=: Recebe true ou false e é opcional
        True: mostra a situação do aluno, se foi boa, razoável ou ruim
        False: Não mostra nada
    """
    dicionario: dict = {}
    dicionario['maior'] = max(nota)
    dicionario['menor'] = min(nota)
    dicionario['media'] = sum(nota) / len(nota)
    if situacao:
        if dicionario['media'] >= 7:
            dicionario['situacao'] = 'Boa'
        elif dicionario['media'] >= 5 or dicionario['media'] < 7:
            dicionario['situacao'] = 'Razoável'
        else:
            dicionario['situacao'] = 'Ruim'
    
    return dicionario

aluno = notas(10, 10, 10, situacao=True)
print(aluno)