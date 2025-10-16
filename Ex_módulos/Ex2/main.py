from conversor import *

temp = float(input("Digite uma temperatura: "))
uni = input("Digite a unidade de medida da temperatura: ").lower()

match uni:
    case "c" : 
        nova_temp = celsius_para_farenheit(temp)
        print(f"A temperatura em Farenheit é: {nova_temp:.2f}°F")
    case "f" : 
        nova_temp = fahrenheit_para_celsius(temp)
        print(f"A temperatura em Celsius é: {nova_temp:.2f}°C")
    case _ : 
        print("Unidade de medida inválida")
        


