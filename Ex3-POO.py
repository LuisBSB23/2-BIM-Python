class Carro:
    def __init__(self, modelo, velocidade=70):
        self.modelo = modelo
        self.velocidade = velocidade

    def acelerar(self, valor):
        self.velocidade += valor
        print(f"{self.modelo} acelerou para {self.velocidade} km/h.")

    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"{self.modelo} reduziu a velocidade para {self.velocidade} km/h.")

    def mostrar_velocidade(self):
        print(f"Velocidade atual do {self.modelo}: {self.velocidade} km/h.")

meu_carro = Carro("Mercedes")

meu_carro.mostrar_velocidade()
meu_carro.acelerar(30)
meu_carro.frear(10)
meu_carro.mostrar_velocidade()
meu_carro.frear(25)  # Testando limite mínimo
meu_carro.mostrar_velocidade()