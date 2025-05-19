# Definição da classe chamada "Aluno"
class Aluno:

    # Método construtor (__init__) que inicializa os atributos do objeto
    def __init__(self, nome, idade):
        # Atributo "nome" do aluno
        self.nome = nome

        # Atributo "idade" do aluno
        self.idade = idade

        # Atributo "notas", uma lista vazia que vai armazenar as notas do aluno
        self.notas = []

    # Método da classe para adicionar uma nota à lista de notas
    def adicionar_nota(self, nota):
        self.notas.append(nota)  # Adiciona a nova nota à lista de notas do aluno

    # Método da classe para calcular a média das notas do aluno
    def calcular_media(self):
        if self.notas:  # Verifica se a lista de notas não está vazia
            # Soma todas as notas e divide pela quantidade de notas
            return sum(self.notas) / len(self.notas)
        else:
            return 0  # Retorna 0 se o aluno não tiver nenhuma nota

# Testar código
'''aluno1 = Aluno("Luis", 20)

aluno1.adicionar_nota(7.2)
aluno1.adicionar_nota(5.1)
aluno1.adicionar_nota(8)

print(f"Nome: {aluno1.nome}")
print(f"Idade: {aluno1.idade}")
print(f"Notas: {aluno1.notas}")
print(f"Média: {aluno1.calcular_media():.2f}")'''

#Teste para inserir com input
# Entrada de dados
nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))

# Criando o objeto aluno
aluno1 = Aluno(nome, idade)

# Adicionando 3 notas
for i in range(1, 4):
    nota = float(input(f"Digite a {i}ª nota: "))
    aluno1.adicionar_nota(nota)

# Exibindo os resultados
print(f"\nNome: {aluno1.nome}")
print(f"Idade: {aluno1.idade}")
print(f"Notas: {aluno1.notas}")
print(f"Média: {aluno1.calcular_media():.2f}")