from random import randint

# computador = randint(0, 10)
# contador = 1
# print("Sou seu computador...")
# print("Acabei de pensar em um numero entre 0 e 10.")
# print("Sera que voce consegue advinhar qual foi? ")

# num = int(input("Qual é seu palpite? "))



# while num != computador:
#     if num < computador:
#         num = int(input("Menos... Tente outra vez: "))
#     elif num > computador:
#         num = int(input("Mais... Tente outra vez: "))
#     contador += 1

# print(f"Parabens.Voce tentou {contador} vezes para acertar a minha escolha que foi {computador} !!")


computador = randint(0, 10)
print("Sou seu computador... Acabei de pensar em um numero entre 0 e 10.")
print("Sera que voce consegue advinhar qual foi? ")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual o seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez")
        elif jogador > computador:
            print("Menos... Tente mais uma vez")
print(f"Acertou com {palpites} tentativas, parabens")