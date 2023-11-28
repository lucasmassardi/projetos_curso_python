valores = []
pares = []
impares = []
while True:
    valores.append(int(input("Digite um valor: ")))
    resp = input("Quer continuar? [S/N]")
    if resp in "Nn":
        break
for i ,v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f"Voce digitou os valores {valores}")
print(f"Os valores pares foram {pares}")
print(f"Os valores impares foram {impares}")