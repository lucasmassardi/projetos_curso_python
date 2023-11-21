n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0
while opcao != 5:
    print("""    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa""")
    opcao = int(input("Qual sua opção? "))
    if opcao == 1:
        print(f"A soma dos valores {n1} + {n2} é {n1 + n2}.")
    elif opcao == 2:
        print(f"A multiplicação dos valores {n1} x {n2} é {n1 * n2}")
    elif opcao == 3:
        if n1 > n2:
            print(f"Entre os numeros {n1} e {n2} o maior é {n1}")
        else:
            print(f"Entre os numeros {n1} e {n2} o maior é {n2}")
    elif opcao == 4:
        print("Informe os numeros novamente")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Fim do programa! Volte sempre!")
    else:
        print("Opçãp invalida tente novamente")