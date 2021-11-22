import random

def jogar():

    mensagem_abertura()
    numero_secreto = define_numero_secreto()
    quantidade_tentativas = escolhe_nivel_jogo()
    rodadas_jogo(numero_secreto, quantidade_tentativas)

def mensagem_abertura():
    print("***************************")
    print("******** Bem vindo ********")
    print("*** Jogo da Adivinhação ***")
    print("***************************")

def define_numero_secreto():
    numero_randomico = round(random.randrange(1, 101))#Definir intervalo de numeros randomicos entre 1 e 100
    numero_secreto = numero_randomico
    return numero_secreto

def escolhe_nivel_jogo():
    quantidade_tentativas = 0

    print("Escolha seu nível de dificuldade: ")
    print("(1) Fácil  (2) Médio  (3) Difícil")
    nivel = int(input("Seu nível é: "))
    #Jogador define o nível do jogo, retornando no total de tentativas/rodadas do jogo:
    if(nivel == 1):
        quantidade_tentativas = 5
    elif(nivel == 2):
        quantidade_tentativas = 4
    elif(nivel == 3):
        quantidade_tentativas = 3
    else:
        print("Digite um número válido para definir o nível de seu jogo.")
    return quantidade_tentativas

def rodadas_jogo(numero_secreto, quantidade_tentativas):
    rodada = 1
    pontos = 1000

    while(rodada <= quantidade_tentativas):
        print("Tentativa {} de {}" .format(rodada, quantidade_tentativas))
        chute = int(input("Digite o seu número: "))#Recebe chute do jogador
        print("O número que você digitou foi: ", chute)

        if (chute < 1 or chute > 100):#tratativa de números chutados fora do intervalo
            print("São válidos números apenas entre 1 e 100.")
            continue

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto

        if(acertou):
            print("Voce acertou na tentativa {}!" .format(rodada))
            print("Você fez {} pontos!" .format(pontos))
            break
        else: #Mensagens para chutes diferentes do numero secreto
            if (rodada == quantidade_tentativas):
                print(f'Você errou! O número secreto era: {numero_secreto}')
            elif(chute_maior):
                print("Você errou! O número secreto é menor que o número digitado.")
                pontos_perdidos = chute - numero_secreto
                pontos -= pontos_perdidos
            else:
                print("Você errou! O número secreto é maior que o número digitado.")
                pontos_perdidos = numero_secreto - chute
                pontos -= pontos_perdidos


        rodada += 1 #incremento do while até atingir a quantidade_tentativas

if(__name__ == "__main__"):
    jogar()