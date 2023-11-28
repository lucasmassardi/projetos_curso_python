mais_18 = 0
homemcadastrado = 0
mulher20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = input("Sexo: [M/F] ").upper()[0].strip()
    if idade >= 18:
        mais_18 += 1
    if sexo == "M":
        homemcadastrado += 1
    if sexo == "F" and idade < 20:
        mulher20 += 1
    resp = " "
    while resp not in "SN":
        resp = input("Quer continuar [S/N] ").strip().upper()[0]
    if resp == "N":
        break
   

print(f"Total de pessoas com mais de 18 anos: {mais_18}")
print(f"Ao todo temos {homemcadastrado} homens cadastrados")
print(f"E temos {mulher20} mulheres com menos de 20 anos")