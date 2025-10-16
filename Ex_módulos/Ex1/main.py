from operacoes import *

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
resultado = 0
op = input("Escolha a operação (+, -, *, /): ")

match op:
    case "+":
       resultado = soma(a,b)
    case "-":
        resultado = subtracao(a,b)
    case "*":
        resultado = multiplicacao(a,b)
    case "/":
        resultado = divisao(a,b)
    case _:
        print("Operação inválida")

print(f"O resultado da operação é: {resultado}")