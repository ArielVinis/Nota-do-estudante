# Importe as bibliotecas necessárias
# Para começar a utilizar o NumPy, é necessário instalá-lo no ambiente Python. Você pode fazer isso facilmente com o comando pip install numpy.
import numpy as np

# Dados dos participantes
participantes = [

{
"nome": "Ariel",
"localizacao": "Japão",
"afiliacao": "Universidade A",
"interesses": ["Tecnologia", "Direito"]
},

{
"nome": "Lara",
"localizacao": "Portugal",
"afiliacao": "Instituto B",
"interesses": ["Direito", "Magistratura"]
},

{
"nome": "Sofis",
"localizacao": "Brasil",
"afiliacao": "Instituto C",
"interesses": ["Psicologia", "Culinária"]
}

# Adicione mais participantes conforme necessário
]

# Usando sets para identificar diferentes regiões dos participantes
regioes = set(participante["localizacao"] for participante in participantes)

# Usando um dicionário para categorizar afiliações
afiliacoes = {}

for participante in participantes:
    afiliacao = participante["afiliacao"]

    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []

    afiliacoes[afiliacao].append(participante["nome"])

    # Usando NumPy para analisar áreas de interesse
    areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante["interesses"]])

    interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)

    area_mais_popular = interesses_unicos[np.argmax(contagem)]

    # Resultados
    print("Regiões dos participantes:", regioes)
    print("Afiliações dos participantes:")

    for afiliacao, nomes in afiliacoes.items():

        print(f"{afiliacao}: {', '.join(nomes)}")
        print("Área de interesse mais popular:", area_mais_popular)