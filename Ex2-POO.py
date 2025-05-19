class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)


# Testando a classe Retangulo
largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))

r1 = Retangulo(largura, altura)

print(f"Área: {r1.calcular_area()}")
print(f"Perímetro: {r1.calcular_perimetro()}")