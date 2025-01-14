class Cidade():

    def __init__(self, nome, população):
        self.nome_cidade = nome
        self.população_cidade = população

class Estado():

    def __init__(self, nome, lista_cidades, sigla):
        self.nome_estado=nome
        self.lista = lista_cidades
        self.sigla_estado=sigla

    def operação(self):
        soma_população = 0
        for cidade in self.lista:
            print("População de %s: %d" % (cidade.nome_cidade, cidade.população_cidade))
            soma_população += cidade.população_cidade
        print("\nPopulação (%s): %d\n" % (self.nome_estado, soma_população))

Curitiba=Cidade("Curitiba", 1829225)
Londrina=Cidade("Londrina", 577318)
Guaratuba=Cidade("Guaratuba", 44098)
São_Paulo=Cidade("São_Paulo", 11895578)
Santos=Cidade("Santos", 429567)
Campinas=Cidade("Campinas", 1185977)
Teresina=Cidade("Teresina", 866000)
Boa_Hora=Cidade("Boa_Hora", 6902)
Piripiri=Cidade("Piripiri", 65538)


paraná=Estado("Paraná", [Curitiba, Londrina, Guaratuba], "PR")
são_paulo=Estado("São_Paulo", [São_Paulo, Santos, Campinas], "SP")
piauí=Estado("Piauí", [Teresina, Boa_Hora, Piripiri], "PI")

paraná.operação()
são_paulo.operação()
piauí.operação()