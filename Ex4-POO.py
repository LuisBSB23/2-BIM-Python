class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para saque.")
        elif valor <= 0:
            print("Valor de saque inválido.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo atual: R${self.saldo:.2f}")

conta = ContaBancaria("João", 500)

conta.exibir_saldo()       # Mostra o saldo atual
conta.depositar(200)       # Depósito válido
conta.sacar(800)           # Tentativa de saque maior que o saldo
conta.sacar(100)           # Saque válido
conta.exibir_saldo()       # Mostra o saldo atualizado
