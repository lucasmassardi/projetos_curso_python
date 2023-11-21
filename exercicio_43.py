peso = float(input("Qual seu peso? "))
altura = float(input("Qual sua altura? "))

imc = peso / (altura * altura)

print(f"Seu IMC é {imc:.1f}.")

if imc < 18.5:
    print("Voce esta abaixo do peso")
elif imc <25:
    print("Voce esta no peso ideal")
elif imc < 30:
    print("Voce esta com sobrepeso")
elif imc < 40:
    print("Voce esta obeso")
else:
    print("Voce esta com obesidade mórbida")
