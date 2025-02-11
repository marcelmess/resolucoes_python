string1 = "AABBEFAATT"                                                        #registra uma string na variavel "string1"
string2 = "BE"                                                                #registra uma outra string na varivavel "string2"
if string2 in string1:                                                        #verifica se a string da varivavel string2 está presente na string2
    posição = string1.find(string2)                                           #registra na variavel "posição" a posição da string2 na string1
    print("%s encontrado na posição %d de %s" % (string2, posição, string1))  #imprime ao usuário
