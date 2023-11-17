salario = float(input("Qual é o slario do funcionario? "))

if salario <= 1250:
    novo = salario * 0.15 + salario
else:
    novo = salario * 0.10 + salario


print(f"Quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f} agora")