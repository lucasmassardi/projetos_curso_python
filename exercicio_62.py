print("Gerador de PA")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao da PA: "))
termo = primeiro #Vai começar com o numero inserido
cont = 1 # Vai contar quantos termos serão
total = 0 # para calcular quantas progressoes foram feitas
mais = 10 #Para criar o input e saber quantas prog a mais o usuario quer
while mais != 0:  #Enquanto o mais nao for 0 vai fazer o laço
    total = total + mais  #Vai acrescentar no total quantas progressoes serao feitas
    while cont <= total:  # Vai repetir o laço até chegar no total
        print(f"{termo} -> ", end="")
        termo += razao
        cont += 1 
    print("PAUSA")
    mais = int(input("Quanto stermos voce quer mostra mais? "))
print(f"Progressão finalizada com {total} termos mostrados.")