from soma import soma
from subtracao import subtracao
from multiplicacao import multiplicacao
from divisao import divisao

# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu
# nos capítulos até aqui no curso.


print("\n******************* Calculadora em Python *******************")

print(
    "Digite a operação desejada:\n"
    "1 - Soma \n"
    "2 - Subtração \n"
    "3 - Multiplicação \n"
    "4 - Divisão "
)

opcao = input("Digite sua opção: ")
num1 = int(input(("Digite o primeiro número: ")))
num2 = int(input(("Digite o segundo número: ")))

if opcao == "1":
    res = soma(num1, num2)
    print(f"{num1} + {num2} = {res}")

elif opcao == "2":
    res = subtracao(num1, num2)
    print(f"{num1} - {num2} = {res}")


elif opcao == "3":
    res = multiplicacao(num1, num2)
    print(f"{num1} * {num2} = {res}")

elif opcao == "4":
    res = divisao(num1, num2)
    print(f"{num1} / {num2} = {res}")

else:
    print("Opção inválida!")
