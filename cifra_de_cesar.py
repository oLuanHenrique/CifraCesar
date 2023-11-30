from funcoes_criptografia import criptografar,descriptografar

def main():
    print("Escolha a operação:")
    print("1. Criptografar")
    print("2. Descriptografar")

    try:
        opcao = int(input())
    except ValueError:
        print("Digite um número válido.")
        return

    if opcao == 1:
        criptografar()
    elif opcao == 2:
        descriptografar()
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
