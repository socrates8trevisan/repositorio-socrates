v1=float(input('Digite o primeiro número: '))
v2=float(input('Digite o segundo número: '))
print("Escolha a operação desejada:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
operacao = input("Digite o número da operação desejada (1/2/3/4): ")
if operacao=='1':
    resultado=v1+v2
    print(f'{v1}+{v2}={resultado}')
elif operacao=='2':
    resultado=v1-v2
    print(f'{v1}-{v2}={resultado}')
elif operacao=='3':
    resultado=v1*v2
    print(f'{v1}*{v2}={resultado}')
elif operacao=='4':
    if num2 != 0:
        resultado=v1/v2
        print(f'{v1}/{v2}={resultado}')
    else:
        print('Divisão por zero não é permitida.')
else:
    print('Operação inválida. Por favor escolha uma operação válida.')