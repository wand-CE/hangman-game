from ast import literal_eval

def dicionario():
    with open('dicionario.txt', 'r') as arquivo:
        dicionario_txt = literal_eval(arquivo.read())
        return dicionario_txt
