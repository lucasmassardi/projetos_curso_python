classificacao = ("palmeiras", "botafogo", "gremio", "red bull bragantino", "atletico-mg", "flamengo", "atletico-pr", "fluminense", "cuiaba", "sao paulo", "corinthians", "fortaleza", "internacional", "santos", "vasco", "cruzeiro", "bahia", "goias", "coritiba", "america-mg")
print(f"Lista de times: {classificacao}")
print("-=" *35)
print(f"Os 5 primeiro colocados são {classificacao[:5]}")
print("-=" *35)
print(f"Os 4 ultimos colocados são {classificacao[16:]}")
print("-=" *35)
print(f"A classificação em ordem alfabetica é {sorted(classificacao)}")
print("-=" *35)
print(f"A posição do coritiba é {classificacao.index('coritiba')+1}ª")