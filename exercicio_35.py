a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima PODEM FORMAR um triangulo!")
else:
    print("Os segmentos acima NAO PODEM FORMAR um trinagulo!")