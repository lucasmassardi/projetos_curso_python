# v1 = int(input("Digite um numero: "))
# v2 = int(input("Digite outro numero: "))
# v3 = int(input("Digite mais um numero: "))
# v4 = int(input("Digite o ultimo numero: "))

# valores = (v1, v2, v3, v4)

# print(f"Voce digitou os valores {valores}")
# print(f"O numero 9 apareceu {valores.count(9)} vezes")
# if valores.count(3) > 0:
#     print(f"O numero 3 apareceu na {valores.index(3)}º posição")
# else:
#     print("O numero 3 não foi digitado em nenhuma posição")
# pares = []
# for valor in valores:
#     if valor % 2 == 0:
#         pares.append(valor)
# if pares == []:
#     print("Nenhum numero par foi digitado")
# else:
#     print(f"Os numeros pares digitados foram {pares}")


num = (int(input("Digite um valor: ")), int(input("Digite outro valor: ")), int(input("Digite mais um valor: ")), int(input("Digite o ultimo valor: ")))
print(f"Voce digitou os valores {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O valopr 3 apareceu na {num.index(3)+1}ª posição")
else:
    print("O valor 3 não foi digitado em nenhuma posição")
print(f"Os valores pares digitados foram ", end=" ")
for n in num:
    if n % 2 == 0:
        print(n)