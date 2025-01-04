while True:
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))

    def múltiplo(a, b):
        if (a%b==0):
            return True
        else:
            return False
    print(múltiplo(n1, n2))