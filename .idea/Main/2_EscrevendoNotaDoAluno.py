Nota_1 = int(input("Digite a primeira nota: "))
Nota_2 = int(input("Digite a segunda nota: "))
Nota_3 = int(input("Digite a terceira nota: "))
Nota_4 = int(input("Digite a quarta nota: "))
#utilizo a função int(), pois, sem ela, o Python entenderia que as notas seriam String

#condição para a aprovação do aluno.
media = (Nota_1+Nota_2+Nota_3+Nota_4)/4

if media >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"


#dadas as notas, mostra a média final e a situação do aluno.
print(f"Média do aluno foi: {media}")
print(f"Situação do aluno: {situacao}")
print("--------------------------------")
#outra forma é sem o "f string"
print("Notas do aluno: ", Nota_1, Nota_2, Nota_3, Nota_4)
print("Média do aluno: ", media)
print("Situação do aluno: ", situacao)