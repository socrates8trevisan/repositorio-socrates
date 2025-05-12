def soma_tres_valores(a, b, c):
    return a + b + c

def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    resultado = soma_tres_valores(num1, num2, num3)
    print(f"A soma dos três valores é: {resultado}")

main()