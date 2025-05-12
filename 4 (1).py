def calcula_area_triangulo(base, altura):
    return (base * altura) / 2

def main():
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    area = calcula_area_triangulo(base, altura)
    print(f"A área do triângulo é: {area}")

main()