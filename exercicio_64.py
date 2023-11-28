# numero = 0
# cont = 0
# soma = 0

# while numero != 999:
#     numero = int(input("Digite um numero [999 para parar]"))
#     cont += 1
#     soma += numero
#     if numero == 999:
#         cont -= 1
#         soma -= numero
# print(f"Voce digitou {cont} numeros. ", end="")
# print(f"E as soma dos numeros digitados é {soma}")





numero = 0
cont = 0
soma = 0
numero = int(input("Digite um numero [999 para parar]: "))

while numero != 999:
    cont += 1
    soma += numero
    numero = int(input("Digite um numero [999 para parar]: "))
print(f"Voce digitou {cont} numeros. ", end="")
print(f"E as soma dos numeros digitados é {soma}")