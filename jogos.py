import adivinhacao
import forca

print("*****************")
print("*** Bem vindo ***")
print("*****************")

print("Digite o número do jogo que você deseja jogar: ") #Menu para escolher jogos
print("(1) Adivinhação  (2) Forca")
jogo = int(input("Jogo número: "))

if(jogo == 1):
    adivinhacao.jogar()
elif(jogo == 2):
    forca.jogar()
