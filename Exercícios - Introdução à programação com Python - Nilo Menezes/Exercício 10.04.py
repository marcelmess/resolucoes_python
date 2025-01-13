class Televisão:
    def __init__(self, canal_inicial, min=2, max=14):
        self.ligada=False
        self.canal= canal_inicial
        self.tamanho=100
        self.marca="lg"
        self.cmin=min
        self.cmax=max
    def muda_canal_para_cima(self):
        if (self.canal + 1 <= self.cmax):
            self.canal+=1
        else:
            self.canal=0
    def muda_canal_para_baixo(self):
        if (self.canal - 1 >= self.cmin):
            self.canal-=1
        else:
            self.canal=0

tv_smart= Televisão(5)
tv_analógica= Televisão(2,50, 100)

for x in range(0, 120):
    tv_smart.muda_canal_para_cima()
print(tv_smart.canal)

for x in range(0,120):
    tv_analógica.muda_canal_para_cima()
print(tv_analógica.canal)