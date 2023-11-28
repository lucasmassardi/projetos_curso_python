continuar = "S"
media = 0
soma = 0
quant = 0
maior = 0
menor = 0


while continuar in "Ss":
    numero = int(input("Digite um numero: "))
    soma += numero
    quant += 1
    if quant == 1:                  #Enquanto so tenho o primeiro numero ele é o maio e menor 
        maio = menor = numero                 
    else:                              
        if numero > maior:          # Aqui vai ser a partir do segundo numero digitado
            maior = numero
        if numero < menor:
            menor = numero
    continuar = input("Quer continuar? [S/N]").upper().strip()[0]
media = soma / quant
print(f"Voce digitou {quant} numeros e a media foi {media:.2f}")
print(f"O maior numero foi {maior} e menor numero foi {menor}.")