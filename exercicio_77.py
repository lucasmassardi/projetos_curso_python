palavras = ("aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro")
for p in palavras: #Aqui separou as paralavras dentro da tupla em outra tupla
    print(f"\nNa palavra {p.upper()} temos ", end ="")
    for letra in p: #Aqui vai separar todas as letras da palavra
        if letra.lower() in "aeiou": #Se tem essas letras ele vai mostrar
            print(letra, end=" ")