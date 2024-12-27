temperatura = [-10, -8, 0, 1, 2, 5, -2, -4]

máximo = temperatura[0]

for e in temperatura:
    if e > máximo:
        máximo = e

print("Temperatura máxima: %d" % máximo)

mínimo = temperatura[0]
for e in temperatura:
    if e < mínimo:
        mínimo = e

print("Temperatura mínima: %d" % mínimo)

média = (máximo + mínimo) / 2

print("A média, considerando a máxima e a mínima: %d" % média)

soma=0
x = 0
if x <= len(temperatura):
    soma+= temperatura[x]
    x+=1

média2= soma / len(temperatura)

print("A média, considerando todos os valores da lista: %d" % média2)


    
