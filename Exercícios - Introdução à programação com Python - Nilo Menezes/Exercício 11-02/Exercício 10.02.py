import sqlite3
from contextlib import closing

with sqlite3.connect("preços.db") as conexão:
    with closing(conexão.cursor()) as cursor:
        cursor.execute("select * from preços")
        while True:
            resultado=cursor.fetchone()
            if resultado == None:
                break
            print("Nome: %s\nPreço: %s" % (resultado))