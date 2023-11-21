num = int(input("Digite um numero inteiro: "))

print("""Escolha uma das bases para conversao:
[1] converter binario
[2] convrter octal
[3] converter hexadecimal""")

opcao = int(input("Sua opcao: "))

if opcao == 1:
    print(f"{num} convertido para binario é igual a {bin(num)[2:]}")
elif opcao == 2:
    print(f"{num} convertido para octal é igual a {oct(num)[2:]}")
elif opcao == 3:
    print(f"{num} convertido para hexadecimal é igual a {hex(num)[2:]}")
else:
    print("Opcao invalida!!!")