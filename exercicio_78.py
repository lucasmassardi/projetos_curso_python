valores = []
maior = 0
menor = 0
for cont in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {cont}: ")))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
                menor = valores[cont]
print(f"Voce digitou {valores}")
print(f"O mair valor digitado foi {maior} nas posiçoes ", end="")
for i, v in enumerate(valores):
     if v == maior:
          print(f"{i}...")
          print()
print(f"O menor valor digitado foi {menor} nas posiçoes ", end="")
for i, v in enumerate(valores):
     if v == menor:
          print(f"{i}...")