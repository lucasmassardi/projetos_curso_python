velocidade = float(input("Qual a velocidade atual do carro? "))
multa = (velocidade -80) *7


if velocidade > 80:
    print("MULTADO! Voce excedeu o limite de velocidade que é de 80Km/h! ")
    print(f"Voce deve pagar uma multa de R${multa:.2f}!")
else:
    print("Tenha um bom dia! Diriga com segurança!")