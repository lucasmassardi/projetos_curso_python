produto = float(input("Qual o valor do produto: "))

desconto = produto * 0.05
valor_final = produto - desconto

print(f"O produto que custava {produto}, na promoção com deconto de 5 % vai custar {valor_final:.2f}.")