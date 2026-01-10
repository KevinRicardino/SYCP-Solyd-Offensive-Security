# Variáveis em letras maiúsculas são usadas por convenção para representar constantes ou menos comumente variáveis globais
# (valores que não devem ser alterados durante a execução do programa).
AGENDA = {
    "guilherme": {
        "tel": "99999-1010",
        "email": "contato@solyd.com.br",
        "endereco": "av. 1"
    },
    "maria": {
        "tel": "99229-2020",
        "email": "maria@solyd.com.br",
        "endereco": "av. 2"
    },
    "joão": {
        "tel": "98267-6060",
        "email": "joao@solyd.com.br",
        "endereco": "av. 3"
    },
}

# Exibe todas as chaves e valores do dicionário
print(AGENDA['maria'])
print("-"*100)
# Exibe apenas o valor da chave chamada
print(AGENDA['maria']['tel'])
print("-"*100)

AGENDA['guilherme']['endereco'] = "Rua das nações"

AGENDA['lucas'] = {
    "tel": "98882-2189",
    "email": "lucas@solyd.com.br",
    "endereco": "av. josé bonifacio",
}

# Difícil visualização se exibir ela diretamente assim
print(AGENDA)
print("-"*100)

# Para remover um item
AGENDA.pop("guilherme")

# Para melhorar a visualização
for contato in AGENDA:
    print(contato)

print("-"*100)
print(AGENDA['lucas'])