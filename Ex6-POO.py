class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R${self.salario:.2f}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)  # Chama o construtor da classe mãe
        self.departamento = departamento

    def exibir_dados(self):
        super().exibir_dados()  # Chama o método da classe mãe
        print(f"Departamento: {self.departamento}")

func = Funcionario("Ana", 3000)
ger = Gerente("Carlos", 8000, "TI")

print("Funcionário:")
func.exibir_dados()

print("\nGerente:")
ger.exibir_dados()
