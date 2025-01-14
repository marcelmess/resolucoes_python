class Conta():
    def __init__(self, clientes, número, saldo = 0):
        self.saldo = saldo
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.saque_verificador= False

    def resumo(self):
        print("CC Número: %s Saldo: %10.2f\n" % (self.número, self.saldo))
        for cliente in self.clientes:
            print("Nome: %s - Telefone: %s\n" % (cliente.nome, cliente.telefone))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -=valor
            self.operações.append(["SAQUE", valor])
            self.saque_verificador = True
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
        print("Limite: %d - Total disponível para saque: %d \n" % (self.limite, self.disponível))
        if self.saque_verificador == True:
            print("Operação de saque realizada")
        else:
            print("Operação de saque não realizada")

class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo = 0, limite=0):
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite
        if self.limite > saldo:
            self.disponível = saldo
        else:
            self.disponível = limite
    def saque(self, valor):
        if self.saldo + self.limite >=valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            self.saque_verificador = True