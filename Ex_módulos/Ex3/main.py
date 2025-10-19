from texto_utils import *

texto = input("Digite o texto: ")
qtd_vogais = contar_vogais(texto)
print(f"O texto tem {qtd_vogais} vogais.")

qtd_palavras = contar_palavras(texto)
print(f"O texto tem {qtd_palavras} palavras.")

texto_invertido = inverter_texto(texto)
print(f"O texto invertido: {texto_invertido}")



