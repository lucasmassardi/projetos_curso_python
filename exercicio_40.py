n1 = float(input("Primeira nota:"))
n2 = float(input("Segunda nota:"))

media = (n1 + n2) / 2
print(f"Sua media foi de {media:.1f}.")

if media < 5.0:
    print("Voce esta REPROVADO!!!")
elif media >= 5.0 and media <= 6.9:
    print("Voce esta em RECUPERACAO!!!")
else:
    print("Voce esta aprovado!!!!")

