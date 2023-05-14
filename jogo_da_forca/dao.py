from ast import literal_eval

def dicionario():
    with open('dicionario.txt', 'r') as arquivo:
        dicionario = literal_eval(arquivo.read())
        return dicionario
