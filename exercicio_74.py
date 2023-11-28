from random import randint

aleatorio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print("Os valores sorteados foram: ", end=" ")
for n in aleatorio:
    print(f"{n} ", end=" ")

print(f"\nO menor valor da lista foi {min(aleatorio)}")
print(f"O maior valor da lista foi {max(aleatorio)}")
