class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def aprovado(self):
        return self.media() >= 7

nome = input("Digite seu nome:")
nota1 = float(input("Digite 1°Nota:"))
nota2 = float(input("Digite 2°Nota:"))

aluno1 = Aluno(nome, nota1, nota2)

print(f"Aluno: {aluno1.nome}")
print(f"Média: {aluno1.media():.2f}")
print("Aprovado?" , "Sim" if aluno1.aprovado() else "Não")

