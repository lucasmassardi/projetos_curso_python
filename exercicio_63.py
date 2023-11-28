print("-" * 30)
print("Sequencia de Fibonacci")
print("-" * 30)

n = int(input("Quantos termos voce quer mostra? "))
t1 = 0#Na sequencia fibonacci sempre o primeiro termo é 0
t2 = 1#Na sequencia fibonacci sempre o segundo termo é 1
print("~" * 30)
print(f"{t1} -> {t2}", end="")#Inicia a sequencia com o padra de 0 e 1
cont = 3 #Começa apartir do 3 termo pois ja temos por padra t 1 e t 2 
while cont <= n:
    t3 = t1 + t2
    print(f" -> {t3}", end="")
    t1 = t2  #Ele vai avançar sempre uma casa para obter o proximo até finaçizar o laço
    t2 = t3
    cont += 1 #  O contador vai adicionando um até finalizar o laço
print(" -> FIM")