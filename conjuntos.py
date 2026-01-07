# 'Conjunto' em inglês é 'set'

conjunto_cores = {"vermelho", "azul", "verde"}

# Conjunto não repete itens, mesmo que ele te deixe adicionar o mesmo item mais de uma vez.
# Este é o motivo dele ser usado em muitas aplicações, por você não querer coisas repetidas.
# Ele é mais avançado e rápido em diversas situações.

conjunto_cores.add("branco")
print("-"*10)

conjunto_cores.add("vermelho")

print(conjunto_cores)
print("-"*10)

conjunto_cores.remove("branco")

print(conjunto_cores)
print("-"*10)

for cores in conjunto_cores:
    print(cores)