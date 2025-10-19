from calculos import *

notas = []

for nota in range(3):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)

media_final = media(notas)
print(f"Média final: {media_final:.1f}")
situacao_final = situacao(media_final)





