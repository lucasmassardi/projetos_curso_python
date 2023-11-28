valores = []
while True:
    v = int(input("Digite um valor: "))
    if v not in valores:
        valores.append(v)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Não vou adicionar")
    continuar = input("Quer continuar? [S/N]: ")
    if continuar in "Nn":
        break
    
valores.sort()
print(f"Voce digitou {valores}")