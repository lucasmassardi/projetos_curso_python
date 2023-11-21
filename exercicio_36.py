valor_casa = float(input("Qual o valor do imóvel? "))
salario = float(input("Qual o seu salario? "))
tempo = int(input("Em quantos anos voce deseja pagar? "))
qtd_parcelas = tempo * 12
valor_parcelas = valor_casa / qtd_parcelas

print(f"Para pagar uma casa de R${valor_casa:.2f} em {tempo} anos, a prestacao sera de R${valor_parcelas:.2f}!")

if valor_parcelas < salario * 0.30:
    print("Emprestimo aprovado")
else:
    print("Emprestimo negado")


