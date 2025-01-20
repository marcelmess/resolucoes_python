import sqlite3

nome=input("Nome do produto: ")
conexão = sqlite3.connect("preços.db")
cursor = conexão.cursor()
cursor.execute("select * from preços where nome = ?", (nome,))
x=0
while True:
    resultado=cursor.fetchone()
    if resultado == None:
        if x == 0:
            print("Produto não encontrado")
        break
    print("Nome do produto: %s\nPreço: %s" % resultado)
    x+=1

cursor.close()
conexão.close()
