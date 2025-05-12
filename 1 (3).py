def mostrar_mensagem_e_numero(mensagem, numero):
    print(f"Mensagem: {mensagem}")
    print(f"Número: {numero}")

def main():
    mensagem = input("Digite uma mensagem: ")
    numero = int(input("Digite um número: "))
    mostrar_mensagem_e_numero(mensagem, numero)

# Chamada da função principal
if __name__ == "__main__":
    main()