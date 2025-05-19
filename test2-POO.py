class aluno:
    def __init__(self,nome,idade,nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota
    def mostrar(self):
        print(f"O nome do aluno é {self.nome}, sua idade é {self.idade} e sua nota é {self.nota}.")
    
aluno1 = aluno("Paulo", 19, 8)
aluno2 = aluno("Maria", 21, 9)
aluno3 = aluno(input("Digite o nome do aluno:"), int(input("Digite a idade:")), int(input("Digite sua nota:")))

aluno1.mostrar()
aluno2.mostrar()
aluno3.mostrar()