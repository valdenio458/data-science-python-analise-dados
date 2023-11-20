# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

# Import
import random
from os import system, name


# Função para limpar a tela a cada execução
def limpa_tela():
    # Windows
    if name == "nt":
        _ = system("cls")

    # Mac ou Linux
    else:
        _ = system("clear")


# Função
def game():
    limpa_tela()

    print("\nBem-vindo(a) ao jogo da forca")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo

    with open("Cap07/arquivo.txt", "r") as file:
        palavras = [linha.strip() for linha in file]

    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    # List compreehension
    letras_descobertas = ["_" for letra in palavra]
    # Número de chances
    chances = 6

    # Lista para as letras erradas
    letras_erradas = []

    # Loop enquanto o número de chances for maior que zero
    while chances > 0:
        # Print
        print(" ".join(letras_descobertas))
        print("\nChances restantes: ", chances)
        print("Letras erradas: ", " ".join(letras_erradas))

        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era", palavra)
            break
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era", palavra)


# Bloco main
if __name__ == "__main__":
    game()
    print("Parabéns. Você está aprendendo programação em Python!")
