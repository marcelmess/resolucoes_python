class Conta:
    def __init__(self, clientes, número, saldo = 0):
        self.saldo = saldo
        self.clientes = clientes
        self.número = número
        self.operações = []
    def resumo(self):
        print("CC Número: %s Saldo: %10.2f" % (self.número, self.saldo))
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -=valor
            self.operações.append(["SAQUE", valor])
        else:
            print("Saldo insuficiente!")
    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])
    def extrato(self):
        print("Extrato CC N° %s\n" % self.número)
        for o in self.operações:
            print("%10s %10.2f" % (o[0], o[1]))
        print("\n Saldo: %10.2f\n" % self.saldo)