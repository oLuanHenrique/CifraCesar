import sys

def cifra_de_cesar(mensagem, deslocamento, operacao):
    resultado = ""

    for char in mensagem:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            novo_char = chr((ord(char) - base + deslocamento * operacao) % 26 + base)
            resultado += novo_char
        else:
            resultado += char

    return resultado

def criptografar():
    mensagem = input("Digite a mensagem a ser criptografada: ")
    deslocamento = int(input("Digite o número de posições para deslocar: "))
    
    if deslocamento <= 0:
        print("O número de posições deve ser um inteiro positivo.")
        return

    mensagem_criptografada = cifra_de_cesar(mensagem, deslocamento, 1)
    print("Mensagem criptografada:", mensagem_criptografada)

def descriptografar():
    mensagem_criptografada = input("Digite a mensagem a ser descriptografada: ")
    deslocamento = int(input("Digite o número de posições que foram deslocadas: "))
    
    if deslocamento <= 0:
        print("O número de posições deve ser um inteiro positivo.")
        return

    mensagem_descriptografada = cifra_de_cesar(mensagem_criptografada, deslocamento, -1)
    print("Mensagem descriptografada:", mensagem_descriptografada)