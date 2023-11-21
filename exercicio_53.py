#Com for
frase = str(input("Digite uma frase: ")).upper().strip()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Temos um palindromo!")
else:
    print("A frase digitada nao é um palindromo")



#Sem for

# frase = str(input("Digite uma frase: ")).upper()
# palavras = frase.split()
# junto = "".join(palavras)
# inverso = junto[::-1]

# print(f"O inverso de {junto} é {inverso}")
# if inverso == junto:
#     print("Temos um palindromo!")
# else:
#     print("A frase digitada nao é um palindromo")


