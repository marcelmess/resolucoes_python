string1 = "AABBEFAATT"
string2 = "BE"
if string2 in string1:
    posição = string1.find(string2)
    print("%s encontrado na posição %d de %s" % (string2, posição, string1))
