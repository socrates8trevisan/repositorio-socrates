# Inicializando as variáveis
soma_pares = 0
soma_impares = 0
contagem_pares = 0
contagem_impares = 0

while True:
    try:
        numero = int(input("Digite um número (digite 0 para encerrar): "))
        
        if numero == 0:
            break  
        
        if numero % 2 ==:
            soma_pares += numero
            contagem_pares += 1
        else:            
            soma_impares += numero
            contagem_impares += 1
            
    except ValueError:
        print("Por favor, digite um número inteiro válido.")


if contagem_pares > 0:
    media_pares = soma_pares / contagem_pares
else:
    media_pares = 0

if contagem_impares > 0:
    media_impares = soma_impares / contagem_impares
else:
    media_impares = 0


print(f"\nMédia dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")