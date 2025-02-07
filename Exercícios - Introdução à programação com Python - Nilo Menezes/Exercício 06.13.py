temperatura = [-10, -8, 0, 1, 2, 5, -2, -4]                            #cria uma lista com valores inteiros 
máximo = temperatura[0]                                                #define uma variável maximo como o índice 0 da lista
for e in temperatura:                                                  #para cada valor da lista, verifica se é maior que o valor da variável máximo
    if e > máximo:                                                     #se for maior, altera o valor da variável para o valor em questão da lista
        máximo = e
print("Temperatura máxima: %d" % máximo)
mínimo = temperatura[0]                                                #define uma variável mínimo como o índice 0 da lista
for e in temperatura:                                                  #para cada valor da lista, verifica se é menor que o valor da variável mínimo
    if e < mínimo:                                                     #se for maior, altera o valor da variável para o valor em questão da lista
        mínimo = e
print("Temperatura mínima: %d" % mínimo)
média = (máximo + mínimo) / 2                                          #calcula a média do maior e do menor valor da lista
print("A média, considerando a máxima e a mínima: %d" % média)
soma=0                                                                 #estabelece uma variável que receberá o valor de cada índice da lista
contador = 0                                                           #estabelece um contador
while contador <= len(temperatura):                                    #esatebelece um loop que rodará enquanto o contador for menor ou igual ao tamanho da lista
    soma+= temperatura[contador]                                       #soma o valor do respectivo índice da lista
    contador+=1                                                        #aumenta em 1 unidade o valor do contador
média2= soma / len(temperatura)                                        #divide a soma obtida pelo número de valores da lista
print("A média, considerando todos os valores da lista: %d" % média2)
