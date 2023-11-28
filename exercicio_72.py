# num = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")


# while True:
#     numero = int(input("Digite um numero entre 0 e 20: "))
#     if numero >= 0 and numero <=20:
#         break
#     if numero < 0 or numero > 20:
#         numero = int(input("Tente novamente. Digite um numero entre 0 e 20: "))

# print(f"Voce digitou o numero {num[numero]}")



# cont = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
# while True:
#     num = int(input("Digite um numero de 0 a 20: "))
#     if 0 <= num <= 20:
#         break
#     print("Tente novamente", end=" ")
# print(f"Voce digitou o numero {cont[num]}")

num = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")


while True:
    numero = int(input("Digite um numero entre 0 e 20: "))
    if numero >= 0 and numero <=20:
        break
    print("Tente novamente.",  end="")

print(f"Voce digitou o numero {num[numero]}")