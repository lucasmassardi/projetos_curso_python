a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
maior = a
menor = a

if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f" O menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")