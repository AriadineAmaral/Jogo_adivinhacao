import random
def jogar():

    abertura_jogo()

    palavra_secreta = carrega_palavra()

    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
           chute_correto(chute,letras_acertadas, palavra_secreta)
        else:
             erros += 1


        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!!")

    else:
        print("Você perdeu!")


def abertura_jogo():
    print("********************************")
    print("Bem vindo ao jogo de Forca")
    print("********************************")

def carrega_palavra():
    with open("palavras.txt", "r") as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def pede_chute():
   chute = input("Qual letra? ")
   chute = chute.strip().upper()
   return chute

def chute_correto(chute,letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


if(__name__ == "__main__"):
    jogar()
