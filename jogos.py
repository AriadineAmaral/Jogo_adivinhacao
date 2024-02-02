import forca
import adivinhacao

def escolhe_jogo():

    print("Forca (1) Adivinhação (2)")
    jogo = int(input("Digite a opção desejada "))

    if (jogo == 1):
        print("Jogando Forca ")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação ")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()