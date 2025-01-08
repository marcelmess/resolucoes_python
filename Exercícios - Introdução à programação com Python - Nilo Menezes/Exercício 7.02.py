string1 = "AAACTBF"
string2 = "CBTAGH"

string2_list = list(string2)
resultado = []

for caractere in string2_list:
    if caractere in string1:
        resultado.append(caractere)

resultado_oficial="".join(resultado)
print(resultado)
print(resultado_oficial)
