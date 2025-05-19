class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


# Testando a classe Pessoa
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

p1 = Pessoa(nome, idade)
p1.apresentar()