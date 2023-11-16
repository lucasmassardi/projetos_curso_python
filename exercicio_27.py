nome = input("Digite seu nome completo; ").strip()
dividir_nome = nome.split()

print("Muito prazer em te conhece ")
print(f"Seu primeiro nome é {dividir_nome[0]}")
print(f"Seu ultimo nome é {dividir_nome[len(dividir_nome)-1]}")
