API_TOKEN = '123456'

nome = 'joao'

def soma(a,b):
    """
    Função para somar!
    """

    return a+b

def print_nome(frase = nome):
    print(frase)

def altera_nome(novo_nome):
    nome = novo_nome

def _print_dict(dicionario):
    for k in dicionario.keys():
        print(f'{k} : {dicionario[k]}')

def pessoa(nome,funcao):
    p = {}
    p['nome'] = nome
    p['funcao'] = funcao

    _print_dict(p)