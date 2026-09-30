import random

numero_secreto = random.randint(1,5)
num_tentativas = 0

print("Bem- vindo ao jogo de adivinhação!\n tente advinhar um número entre 1 e 1000.")

while True:
    palpite = input("\nDigite um numero: " )
    num_tentativas=+1

    if (palpite == numero_secreto):
        print("👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏")
    elif (palpite > numero_secreto):
      print("o numero secreto e maior!")
    else:
        print("O numero secreto e menor!")  





        