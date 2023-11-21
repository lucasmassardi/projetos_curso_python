n = int(input("Informe um numero: "))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        total += 1
    else:
        ...
    print(f"{c}", end=" ")
print(f"O numero {n} foi divisivel {total} vezes")

if total == 2:
    print("E por isso ele é PRIMO!")
else:
    print("E por isso ele NAO É PRIMO!")