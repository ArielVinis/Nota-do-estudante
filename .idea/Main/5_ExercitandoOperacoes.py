# Tupla de convidados
convidados = ("Alice", "Bob", "Carol", "David", "Eve")

# Lista de confirmações
confirmados = ["Bob", "David"]

# Identificar quem ainda não confirmou
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

# Exibir os convidados que ainda não confirmaram
print("Convidados que ainda não confirmaram:")

for pessoa in nao_confirmados:

    print(pessoa)

# Enviar lembretes aos não confirmados
print("\n -Enviando lembretes para os convidados que ainda não confirmaram.-")