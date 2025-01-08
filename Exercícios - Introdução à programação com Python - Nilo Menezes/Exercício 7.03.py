string1 = "CTAHSOK"
string2 = "ABCCLMC"
string3 = "BTQRS"

string1_list = list(string1)
string2_list = list(string2)
string3_list = list(string3)

resultado = []

for caractere in string1:
    if caractere not in string2 and caractere not in string3:
        resultado.append(caractere)

for caractere in string2:
    if caractere not in string1 and caractere not in string3:
        resultado.append(caractere)

for caractere in string3:
    if caractere not in string2 and caractere not in string1:
        resultado.append(caractere)

resultado_oficial="".join(resultado)
print(resultado)
print(resultado_oficial)
