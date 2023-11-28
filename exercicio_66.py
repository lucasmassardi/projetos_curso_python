numero = 0
cont = 0
soma = 0

while True:
    numero = int(input("Digite um numero (999 para parar):  "))
    cont += 1
    if numero == 999:
        break
    soma += numero

print(f"A soma dos {cont} valores foi {soma}")
