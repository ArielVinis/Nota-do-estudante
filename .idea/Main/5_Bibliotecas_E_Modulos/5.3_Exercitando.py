import matplotlib.pyplot as plt

# Dados de exemplo
# Ordene da maneira correta
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Novembro']
atendimentos = [120, 90, 150, 80, 200, 350]

# Criar um gráfico de barras
# Você pode escolher a cor que quiser, como sou daltônito, prefiro cores frias :)
plt.bar(meses, atendimentos, color='royalblue')

# Adicionar rótulos aos eixos
plt.xlabel('Mês')
plt.ylabel('Atendimentos (no total)')

# Adicionar um título ao gráfico
plt.title('Atendimentos Mensais')

# Mostrar o gráfico
plt.show()