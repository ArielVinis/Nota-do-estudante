class Animal:

    def __init__(self, nome):
        self.nome = nome
    def fazer_barulho(self):
        pass

class Cachorro(Animal):
    def fazer_barulho(self):
        return "Latir"
class Gato(Animal):
    def fazer_barulho(self):
        return "Miar"


# Criando objetos das classes-filhas
rex = Cachorro("Rex")
whiskers = Gato("Whiskers")

# Chamando o método fazer_barulho em objetos
print(f"{rex.nome} faz: {rex.fazer_barulho()}")  # Saída: "Rex faz: Latir"

print(f"{whiskers.nome} faz: {whiskers.fazer_barulho()}")  # Saída: "Whiskers faz: Miar"