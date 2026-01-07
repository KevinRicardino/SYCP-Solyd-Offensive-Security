dicionario = {
    "tijolo": "objeto para montar muros",
    "constituição": "lei máximo do Brasil"
}

pessoas = {
    "guilherme": 19,
    "maria": 17,
    "joão": 20
}

print(dicionario['constituição'])
print(pessoas['maria'])
print("-"*10)

# Iterando direto no dicionário (chaves)
for pessoa in pessoas:
    print(pessoa)
print("-"*10)

# Iterando pelos valores das chaves
for pessoa in pessoas.values():
    print(pessoa)
print("-"*10)

# Exibindo a chave e o valor
for pessoa in pessoas:
    print(pessoa, pessoas[pessoa])
print("-"*10)
