# num = int(input("Informe um numero para calcular fatorial: "))

# cont = 1
# resultado = 1

# while cont <= num:
#     resultado *= cont
#     cont += 1
# print(resultado)


n = int(input("Informe um numero para saber seu fatorial: "))
c = n # contador é inicial com numero pois fatorial se calcula do numero multiplicando ate o 1
f = 1 #Fatorrial tem que inicir em um pois vai multiplicar
print(f"Calculando {n}! = ", end="")
while c > 0:
    print(f"{c}", end="")# Para aparecer todos os numero
    print(" x " if c > 1 else " = ", end="") #Para colocar um x entre os numeros e qdo chegar no 1 cloca o =
    f *= c # Vai multiplicar do contador a cada laço
    c -= 1 # Para o contador ir diminuindo o numero para o calculo do fatorial
print(f"{f}")