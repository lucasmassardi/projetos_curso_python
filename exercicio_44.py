produto = float(input("Valor da compra: "))
print("""FORMAS DE PAGAMENTO
[ 1 ] á vista dinehiro/cheque
[ 2 ] á vista cartao
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartao""")
opcao = int(input("Qual é a opcao? "))

if opcao == 1:
    valor = produto - (produto * 0.10)
    print(f"Sua compra de R${produto:.2f} vai custar R${valor:.2f}")
elif opcao == 2:
    valor = produto -(produto * 0.05)
    print(f"Sua compra de R${produto:.2f} vai custar R${valor:.2f}")
elif opcao == 3:
    print(f"Sua compra de R${produto:.2f} vai custar R${produto:.2f} parcelado em 2x")
elif opcao == 4:
    valor = produto + (produto * 0.20)
    qtd_parcelas = int(input("Quantas parcelas? "))
    print(f"Sua compra sera parcela em {qtd_parcelas}x de {valor / qtd_parcelas:.2f}")
    print(f"Sua compra de R${produto:.2f} vai custar R${valor:.2f}")



