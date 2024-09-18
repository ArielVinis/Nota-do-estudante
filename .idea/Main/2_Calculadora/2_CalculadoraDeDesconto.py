# Solicita ao usuário que insira o valor do produto e o percentual de desconto

valor_produto = float(input("Digite o valor de um produto: R$ "))
percentual_desconto = float(input("Digite um percentual de desconto: % "))


# Verifica se o percentual de desconto está dentro dos limites aceitáveis (0-100%)
if percentual_desconto < 0 or percentual_desconto > 100:
    print("Erro: O percentual de desconto deve estar entre 0% e 100%.")

else:
    # Calcula o valor do desconto
    desconto = valor_produto * (percentual_desconto / 100)

    # Calcula o valor final da compra
    valor_final = valor_produto - desconto

    # Exibe o valor final da compra
    print(f"Valor com desconto: R$ {valor_final:.2f}")