string1 = "TTAACHUJSILAJSDJHISDH"

string1_lista ="".join(string1)

resultado=[]
for caractere in string1_lista:
    if caractere in string1_lista and caractere not in resultado:
        resultado.append(caractere)

contador = []
for unidade in resultado:
    contador.append(string1_lista.count(unidade))

resultado_oficial="".join(resultado)

contador2 = 0
for caractere in resultado:
    print("Há %d unidades da letra %s" % (contador[contador2], caractere))
    contador2+=1
