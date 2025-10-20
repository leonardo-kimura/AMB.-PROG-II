from produtos import *
from utils import *

while True:
    print("\n### MENU ###") 
    print("1 - Adicionar Produto")
    print("2 - Listar Produtos")
    print("3 - Buscar Produto")
    print("0 - Sair")


    try:
        op = int(input("Selecione uma das opções: "))
    except ValueError:
        print("Opção inválida! Por favor, digite um número.")
        continue 

    match op:
        case 1:
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            adicionar_prod(nome, preco)
        
        case 2:
            print("### Listando todos os produtos ###")
            listar_prod() 

        case 3:
            nome_busca = input("Qual produto você deseja buscar? ")
            buscar_prod(nome_busca)

        case 0:
            print("Saindo do sistema. Até logo!")
            break