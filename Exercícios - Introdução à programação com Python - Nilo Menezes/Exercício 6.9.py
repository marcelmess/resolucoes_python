2
L=[15,7,27,39]
p=int(input("Digite o primeiro valor a procurar: "))
p2=int(input("Digite o segundo valor a procurar: "))
x=0

while x<len(L):
    if L[x]==p:
        print("%d achado na posição %d" % (p,x))
        break
    
    elif L[x]==p2:
        print("%d achado na posição %d" % (p2, x))
        break
    x+=1
