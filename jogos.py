import forca
import adivinhacao

def escolhe_jogo():
    print("*************************")
    print("***Escolha o seu jogo!***")
    print("*************************")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo?"))


    if jogo == 1:
        print("Você selecionou jogo da Forca")
        forca.jogar()
    elif jogo == 2:
        print("Você selecionou jogo de adivinhação")
        adivinhacao.jogar()
    else:
        print("Número inválido, selecione (1) ou (2)")

if __name__ == "__main__":
    escolhe_jogo()
