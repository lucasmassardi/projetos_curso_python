# a = float(input("Primeiro segmento: "))
# b = float(input("Segundo segmento: "))
# c = float(input("Terceiro segmento: "))

# if a < b + c and b < a + c and c < a + b:
#     print("Os segmentos acima PODEM FORMAR um triangulo!")
#     if a == b and b == c:
#         print("Seu triangulo sera equilatero")
#     elif a == b or b == c or a == c:
#         print("Seu triangulo sera isoceles")
#     elif a != b and b != c and a!= c:
#         print("Seu triangulo é escaleno")
# else:
#     print("Os segmentos acima NAO PODEM FORMAR um trinagulo!")


a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima PODEM FORMAR um triangulo!")
    if a == b and b == c:
        print("Seu triangulo sera equilatero")
    elif a != b and b != c and a!= c:
        print("Seu triangulo é escaleno")
    else:
        print("Seu triangulo sera isoceles")
    
else:
    print("Os segmentos acima NAO PODEM FORMAR um trinagulo!")


