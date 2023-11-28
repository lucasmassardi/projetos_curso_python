valor = int(input("Qual valor voce quer sacar? R$"))
total = valor
ced = 50  #Começa com a maior cedula
totalced = 0

while True:
    if total >= ced: #Se o total for menor que a cedula , Verifico quantas vezes consigo tirar do valor total
        total -= ced  #Tiro o valor da cedula e sobra esse resto
        totalced += 1  # Contador de cédulas
    else:
        print(f"Total de {totalced} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break

