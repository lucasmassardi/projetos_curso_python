dia = int(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))

valor_dia = 60 * dia
valor_km = 0.15 * km

total = valor_dia + valor_km

print(f"O total a pagar é de R${total:.2f}.")