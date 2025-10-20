from utils import *
Estoque = []

def adicionar_prod(nome,preco):
    produto = {
        'nome': nome,
        'preco': preco
    }
    Estoque.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso!")

def listar_prod():
    if not Estoque:
        print("Estoque vazio.")
    for prod in Estoque:
        print(f"Nome: {prod['nome']}, Preço: {formatar_moeda(prod['preco'])}")

def buscar_prod(nome):
    for produto in Estoque:
        if produto['nome'] == nome:
            print("Produto encontrado!")
            return
    print(f"Produto '{nome}' não encontrado no estoque.")