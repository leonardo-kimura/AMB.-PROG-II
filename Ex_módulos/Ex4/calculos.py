def media(notas):
    media = 0
    for nota in notas:
        media = media + nota
    return media/3

    
def situacao(media):
    if media > 6:
        print("Aluno Aprovado")
    elif media < 6:
        print("Aluno Reprovado")

