string1 = str(input("Digite: "))
string2 = str(input("Digite de novo: "))

string1_lista = list(string1)
string2_lista = list(string2)

for caractere in string2_lista:
    if caractere in string1:
        string1_lista.remove(caractere)

resultado = "".join(string1_lista)
print(resultado)
