class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def vender(self, qtd):
        if qtd <= 0:
            print("Quantidade inválida para venda.")
        elif qtd > self.quantidade:
            print(f"Estoque insuficiente. Disponível: {self.quantidade}")
        else:
            self.quantidade -= qtd
            print(f"Venda de {qtd} unidades realizada com sucesso.")

    def repor(self, qtd):
        if qtd <= 0:
            print("Quantidade inválida para reposição.")
        else:
            self.quantidade += qtd
            print(f"{qtd} unidades adicionadas ao estoque.")

    def exibir_estoque(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Estoque: {self.quantidade} unidades")

p1 = Produto("Caneta", 2.50, 100)

p1.exibir_estoque()
p1.vender(30)
p1.exibir_estoque()
p1.vender(80)   # Excede o estoque
p1.repor(50)
p1.exibir_estoque()
