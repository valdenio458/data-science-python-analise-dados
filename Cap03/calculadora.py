num1 = float(input("Digite o primeiro némro: "))
num2 = float(input("Digite o segundo número: "))
operacao = str(input("Digite a operação: (+, -, *, /)"))

if operacao == "+":
    res = num1 + num2
    print(f"A soma é {res}")
elif operacao == "-":
    res = num1 - num2
    print(f"A diferença é {res}")
elif operacao == "*":
    res = num1 * num2
    print(f"A multiplicação é {res}")
elif operacao == "/":
    res = num1 / num2
    print(f"A divisão é {res}")
else:
    print("Operação inválida!")
