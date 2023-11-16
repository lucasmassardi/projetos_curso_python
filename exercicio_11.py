a = float(input("Altura da parede: "))
l = float(input("Largura da parede: "))

area = a * l
qtd_tinta = area / 2

print(f"Sua parede tem a dimensao de {a} x {l} e sua area é {area:.2f}m2.")
print(f"Para pintar essa parede, voce precisara de {qtd_tinta:.2f}l de tinta")
