lista = [5, 10, 36, 76, 93, 3, 24, 55]

fim = len(lista)

while fim > 1:
    trocou = False
    x = 0
    while x<(fim-1):
        if lista[x] < lista[x+1]:
            trocou = True
            temp = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = temp
        x+=1
    if not trocou:
        break
    fim -= 1
print(lista)
for valor in lista:
    print(valor)
