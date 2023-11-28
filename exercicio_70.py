total = 0
maisdemil = 0
maisbarato = 0
cont = 0
produtobarato = " "
while True:
    produto = input("Nome do produto: ").strip()
    preco = float(input("Valor do produto: R$"))
    total += preco
    cont += 1
    continuar = input("Quer continuar? [S/N]").strip().upper()[0]
    if continuar == "N":
        break
    if preco > 1000:
        maisdemil += 1
    if cont == 1:     #Quando o cont for o primeiro o mais barato se torna o preco mais barato e o produto o mais barato
        maisbarato = preco
        produto = produto
    else:
        if preco < maisbarato:   #Quando o preco é menos que o mais barato o mais barato se torna preco e o produto mais barato se torna barato e assim ate terminar o laço
            maisbarato = preco
            produtobarato = produto
    
print(f"O total de compras foi R${total:.2f}")
print(f"Temos {maisdemil} produtos custando mais de R$ 1000.00")
print(f"O produto mais barato foi {produtobarato} que custa R${maisbarato:.2f}")
