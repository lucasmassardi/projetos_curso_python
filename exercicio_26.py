f = input("Digite uma frase: ").upper().strip()
qtd= f.count("A")
a_primeira = f.find("A")+1
a_ultima = f.rfind("A")+1

print(f"A letra A aparece {qtd} vezes na frase.")
print(f"A primeira letra A apareceu na posição {a_primeira}")
print(f"A ultima letra A apareceu na posicao {a_ultima}")