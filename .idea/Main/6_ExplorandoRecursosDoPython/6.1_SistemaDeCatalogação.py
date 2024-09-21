import matplotlib.pyplot as plt

# Classe para representar um livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"{self.titulo} escrito por {self.autor}, foi publicado em {self.ano_publicacao}"

# Criar uma lista de livros
biblioteca = []

# Lista para armazenar os anos de publicação
anos = []

# Função para adicionar um livro à biblioteca
def adicionar_livro(titulo, autor, ano_publicacao):
    novo_livro = Livro(titulo, autor, ano_publicacao)
    biblioteca.append(novo_livro)
    anos.append(ano_publicacao) # Adiciona o ano à lista 'anos'

    print(f"O livro '{titulo}' foi adicionado à biblioteca.")

# Função para listar todos os livros na biblioteca
def listar_livros():
    print()

    for livro in biblioteca:
        print(livro)

# Adicionar alguns livros à biblioteca
adicionar_livro("Os segredos da mente milionaria", "T. Harv Eker", 1605)
adicionar_livro("Verity", "Coolen Hoover", 1813)
adicionar_livro("Darkside", "N.P. Lovecraft", 1893)
adicionar_livro("Orgulho e Preconceito", "jane Austen", 1967)
adicionar_livro("1984", "Geroge Orwell", 1949)
adicionar_livro("As intermitências da morte", "José Saramago", 2005)

# Listar todos os livros na biblioteca
listar_livros()

# Criar um gráfico de livros por ano
anos = list(set(anos)) # Remove duplicatas dos anos
anos.sort()

# Contagem de livros por ano
contagem_por_ano = [anos.count(ano) for ano in anos]

# Criar um gráfico de linha
plt.plot(anos, contagem_por_ano, marker='o', linestyle='-')
plt.xlabel('Ano de Publicação')
plt.ylabel('Número de Livros')
plt.title('Distribuição de Livros na Biblioteca por Ano de Publicação')

# Adicionar rótulos aos pontos de dados
for i, valor in enumerate(contagem_por_ano):
    plt.text(anos[i], valor, str(valor), ha='center', va='bottom')

plt.grid(True)

plt.show()