def area(a, b):
    m = a * b
    print(f"A area de um terreno de {a}x{b} é de {m}m")


print("  Controle de Terrenos")
print("-" * 30)
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))

area(largura, comprimento)
