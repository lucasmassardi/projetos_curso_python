nasc = int(input("Digite o ano de nascimento: "))
idade = 2023 - nasc

print(f"Voce nasceu em {nasc} e tem {idade} anos, logo abaixo sera listada sua categoria.")

if idade <= 9:
    print("Sua categoria sera MIRIM!")
elif idade > 9 and idade <= 14:
    print("Sua categoria é INFANTIL!")
elif idade > 14 and idade <= 19:
    print("Sua categoria é JUNIOR!")
elif idade > 19 and idade <= 25:
    print("Sua categoria é SENIOR!")
else:
    print("Sua categoria é MASTER!!!")