mais18 = 0
homem = 0
mulher20 = 0

while True:
    idade = int(input("Idade: "))
    sexo = input("Sexo: [M/F] ").strip().upper()[0]
    continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar == "N":
        break
    if idade >= 18:
        mais18 += 1
    if sexo == "M":
        homem += 1
    if sexo == "F" and idade < 20:
        mulher20 += 1

print(f"Total de pessoas com mais de 18 anos: {mais18}")
print(f"Ao todo temos {homem} homens cadastrados")
print(f"E temos {mulher20} mulheres com menos de 20 anos")
