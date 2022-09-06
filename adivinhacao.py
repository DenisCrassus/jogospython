import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Díficil")

    #Nivel de dificuldade
    nivel = int(input("Defina um nível: "))
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #Quantidade de tentativas e resultado
    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute = int(input("Digite um número entre 1 e 100: "))
        print(f"Você digitou {chute}")

        if chute < 1 or chute > 100:
            print("Número inválido, digite um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f"Você ganhou e fez {pontos} pontos!")
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior do que o número correto.")
                if rodada == total_de_tentativas:
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            elif menor:
                print("Voce errou! O seu chute foi menor que o número correto.")
                if rodada == total_de_tentativas:
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute) # funçao abs(absoluto) para evitar números negativos.
            pontos = pontos - pontos_perdidos




    print("Fim do jogo!")

#NECESSARIO CHAMAR A FUNÇÃO (DEF JOGAR()) PARA QUE EXECUTE O JOGO.

if __name__ == "__main__":
    jogar()