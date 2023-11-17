from random import randint
from time import sleep

computador = randint(0, 5)

print("--=" *20)
print("Vou pensar em um numero entre o e 5. Tente advinhar ...")
print("--=" *20)

num = int(input("Em que numero eu pensei? "))
print("PROCESSANDO ... ")
sleep(3)

if num == computador:
    print("Parabéns, voce conseguiu me vencer!")
else:
    print(f"GANHEI! Eu pensei no numero {computador} e não no {num}!")


