sexo = input("Informe seu sexo: [M/F] ").upper()[0].strip()
while sexo not in  "M" and sexo not in "F":
    sexo = input("Dados invalidos.Por favor, informe seu sexo: ").upper()[0].strip()

print(f"Sexo {sexo} registrado com sucesso")