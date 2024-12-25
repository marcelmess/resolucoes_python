#exercício 5.22

while True:
    tabuada=1
    print("Qual operação a tabuada deve apresentar? ['adição', 'subtração', 'multiplicação' ou 'divisão']")
    entrada=str(input(""))
    if entrada == "adição":
        operação = "+"
    elif entrada == "subtração":
        operação = "-"
    elif entrada == "multiplicação":
        operação = "*"
    elif entrada == "divisão":
        operação = "/"
    while tabuada <=10:
        número = 1
        while número <=10:
            if operação == "+":
                resultado = tabuada + número
                print("%d %s %d = %d" % (tabuada, operação, número, resultado))
                número+=1
            elif operação == "-":
                resultado = tabuada - número
                print("%d %s %d = %d" % (tabuada, operação, número, resultado))
                número+=1
            elif operação == "*":
                resultado = tabuada * número
                print("%d %s %d = %d" % (tabuada, operação, número, resultado))
                número+=1
            elif operação == "/":
                resultado = tabuada / número
                print("%d %s %d = %d" % (tabuada, operação, número, resultado))
                número+=1
        tabuada+=1
                  
    
