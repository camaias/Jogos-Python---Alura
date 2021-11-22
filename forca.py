import random

def jogar():

    mensagem_abertura()
    palavra_secreta = escolhe_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = chute_jogador()

        if(chute in palavra_secreta):
             marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros = marca_chute_errado(erros)
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(enforcou):
        print("*** Você foi enforcado! :( ***")
    if(acertou):
        print(("*** Você acertou! :) ***"))


def mensagem_abertura():
    print("*********************")
    print("***** Bem vindo *****")
    print("*** Jogo da Forca ***")
    print("*********************")

def escolhe_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    letras_acertadas =  ["_" for letra in palavra_secreta]
    return letras_acertadas

def chute_jogador():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (letra == chute):
            letras_acertadas[index] = letra
        index += 1

def  marca_chute_errado(erros):
    erros += 1
    print("Erro número {} de 7." .format(erros))
    return erros

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



if(__name__ == "__main__"):
    jogar()
