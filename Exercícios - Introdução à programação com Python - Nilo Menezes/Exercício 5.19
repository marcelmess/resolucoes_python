#exercício 5.19
#python

valor=float(input("Digite o valor a pagar: "))
unidades=0
atual=200.00
apagar=valor

while True:
    if atual<=apagar:
        apagar-=atual
        unidades+=1
    else:
        print("%d unidade(s) de R$%3.2f" % (unidades, atual))
        if apagar == 0:
            break
        elif atual == 200.00:
            atual = 100.00
        elif atual == 100.00:
            atual = 50.00
        elif atual == 50.00:
            atual = 20.00
        elif atual == 20.00:
            atual = 10.00
        elif atual == 10.00:
            atual = 5.00
        elif atual == 5.00:
            atual = 1.00
        elif atual == 1.00:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.25
        elif atual == 0.25:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.01
        elif atual == 0.01:
            atual = 0
        unidades=0
