
ano_nascimento = int(input("Qual o ano do seu nascimento? "))
idade = 2023 - ano_nascimento

print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em 2023")

if idade < 18:
    print(f"Esta quase na hora de se alistar, faltam {18 - idade} anos para voce se alistar!! Voce deve se alistar em {ano_nascimento + 18}")
elif idade == 18:
    print(f"Esta na hora de se alistar voce ja esta com {idade} anos, bora la!!!")
else:
    print(f"Voce ja passou {idade - 18} anos do prazo de alistamento!!!! Voce deveria ter se alistado em {18 + ano_nascimento}, bora la !!!!")



# from datetime import date 

# atual = date.today().year
# nasc = int(input("Ano de nascimento:"))
# idade = atual - nasc

# print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}.")

# if idade == 18:
#     print(f"Voce tem que se alistar imediatamente!")
# elif idade < 18:
#     saldo = 18 - idade
#     print(f"Ainda faltam {saldo} anos para o alistamento!")
#     ano = atual + saldo
#     print(f"Seu alistamento sera em {ano}")
# elif idade > 18:
#     saldo = idade - 18
#     print(f"Voce ja deveria ter se alistado ha {saldo} anos!")
#     ano = atual - saldo
#     print(f"Seu alistamento foi em {ano}!")
