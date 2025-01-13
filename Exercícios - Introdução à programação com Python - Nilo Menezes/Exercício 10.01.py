class Televisão:
    def __init__(self):
        self.ligada=False
        self.canal=2
        self.tamanho=100
        self.marca="lg"


tv_smart= Televisão()
tv_analógica= Televisão()

print(tv_smart.tamanho)
print(tv_analógica.marca)