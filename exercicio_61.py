# print("="*20)
# print("    10 TERMOS DE UMA PA")
# print("="*20)

# n1 = int(input("Primeiro termo: "))
# n2 = int(input("Razao: "))
# decimo = n1 + (10 - 1) * n2

# for c in range(n1, decimo + n2, n2):
#     print(c, end=" -> ")
# print("ACABOU!!")

print("Gerador de PA")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao da PA: "))
termo = primeiro #Vai começar com o numero inserido
cont = 1 # Vai contar quantos termos serão

while cont <= 10:
    print(f"{termo} -> ", end="")
    termo += razao
    cont += 1 
    