pesomaior = 0
pesomenor = 0

for pessoas in range(1, 6):
    peso = float(input(f"Qual o peso da {pessoas}ª pessoa? "))
    if pessoas == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso

print(f"O maior peso é {pesomaior}kg e o menor peso é {pesomenor}kg")