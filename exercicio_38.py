n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

if n1 > n2:
    print(f"O primeiro valor {n1} é maior!")
elif n2 > n1:
    print(f"O segundo valor {n2} é maior!")
else:
    print(f"Não existe valor maior o valor {n1} e {n2} são iguais!")
