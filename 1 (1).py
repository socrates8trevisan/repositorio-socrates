contador = 0
soma = 0
maiores_que_20 = 0

while True:
    
    try:
        valor = float(input("Digite um valor real (ou 'fim' para encerrar): "))
    except ValueError:
        
        entrada = input("Digite um valor real (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break
        else:
            print("Valor inválido, por favor digite um número real.")
            continue
    
    contador += 1
    soma += valor
    if valor > 20:
        maiores_que_20 += 1

if contador > 0:
    media = soma / contador
else:
    media = 0

print(f"\nQuantidade de valores digitados: {contador}")
print(f"Soma dos valores digitados: {soma:.2f}")
print(f"Média aritmética dos valores digitados: {media:.2f}")
print(f"Quantidade de valores maiores que 20: {maiores_que_20}")