from outro_clientes import Cliente
from outro_conta import Conta

joão=Cliente("João da Silva", "777-1234")
maria=Cliente("Maria da Silva", "555-4321")

joão=Conta([joão], 6, 800)
maria=Conta([maria], 50, 500)

joão.saque(50)
joão.saque(190)

maria.deposito(300)
maria.deposito(95.15)
maria.saque(250)

joão.extrato()
maria.extrato()

joão.resumo()