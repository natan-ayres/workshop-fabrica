class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f'seu saldo: {self.saldo}')

    def dep(self, dinheiro):
        self.saldo += dinheiro

    def sac(self, valor):
        if self.saldo < valor:
            print(" Você não pode sacar")
        else:
            self.sac -= valor


pessoa = ContaBancaria('Natan', 0)

pessoa.dep(100)
pessoa.mostrar_saldo()
pessoa.sac(50)
pessoa.mostrar_saldo()
    



