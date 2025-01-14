from outro_conta import Conta, ContaEspecial
from outro_clientes import Cliente

joão=Cliente("João da Silva", "3277-1234")
maria=Cliente("Maria da Silva", "23234-4321")
josé=Cliente("José do Piseiro", "92837-0923")

conta1 = Conta([joão], 6, 800)
conta2 = Conta([maria], 50, 500)
conta3 = ContaEspecial([joão, maria], 2, 500, 100)
terceiro = Conta([joão, josé], 2, 500)

conta3.deposito(50)
conta3.deposito(33.33)
conta3.saque(0.33)

conta1.resumo()
conta3.resumo()
conta2.resumo()
terceiro.resumo()

conta3.extrato()