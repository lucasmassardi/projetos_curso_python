distancia = float(input("Digite a distancia da sua viagem em Km: "))

d_200 = distancia * 0.50
d_mais_200 = distancia * 0.45

if distancia <= 200:
    print(f"Voce esta prestes a começar uma viagem de {distancia}Km")
    print(f"E o preço da sua passagem sera de R${d_200:.2f}.")
else:
    print(f"Voce esta prestes a começar uma viagem de {distancia}km")
    print(f"E o preço da sua passagem sera de R${d_mais_200:.2f}")