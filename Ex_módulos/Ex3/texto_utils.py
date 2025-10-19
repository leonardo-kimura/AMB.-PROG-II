def contar_vogais(texto: str) -> int:
    vogais_validas = "aeiou"
    cont = 0
    for letra in texto:
        if letra.lower() in vogais_validas:
            cont+=1
    return cont

def contar_palavras(texto):
    palavras = texto.split()
    numero_palavras = len(palavras)
    return numero_palavras

def inverter_texto(texto):
    texto = texto[::-1]
    return texto

