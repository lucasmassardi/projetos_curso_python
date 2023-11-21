totmaior = 0
totmenor = 0

for pess in range(1, 8):
    ano_nasc = int(input(f"Em que ano a {pess}ª pessoa nasceu? " ))
    idade = 2023 - ano_nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f"Ao todo tivemos {totmaior} pessoas maiores de idade")
print(f"E tambem tivemos {totmenor} pessoas menores de idade")