
def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"
def verifica_triangulo():
    print("Verificador de Triângulo")
    a = float(input("Digite o comprimento do lado a: "))
    b = float(input("Digite o comprimento do lado b: "))
    c = float(input("Digite o comprimento do lado c: "))
    if (a + b > c) and (a + c > b) and (b + c > a):
        tipo = tipo_triangulo(a, b, c)
        print(f"Os lados formam um triângulo {tipo}.")
    else:
        print("Os lados não podem formar um triângulo.")
verifica_triangulo()


