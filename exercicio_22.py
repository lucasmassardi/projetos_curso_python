nome_complelto = input("Digite seu nome completo: ").strip()
nome_maisusculas = nome_complelto.upper()
nome_minuscula = nome_complelto.lower()
nome_total = (len(nome_complelto) - nome_complelto.count(" "))
divisao_nome = nome_complelto.split()
primeiro_nome = divisao_nome[0]
qtd_letras = (len(divisao_nome[0]))


print(f"Seu nome em maiusculas é {nome_maisusculas}")
print(f"Seu nome em minusculas é {nome_minuscula}")
print(f"Seu nome tem ao todo tem {nome_total} letras")
print(f"Seu primeiro nome é {primeiro_nome} e ele tem {qtd_letras} letras")