import mariadb
import sys

def imprime(self):

    #contacts = []

    cur.execute( "SELECT matricula, nome, idade FROM mysql.cadastrar_aluno",)
    print("w")
    for (matricula, nome, nascimento) in cur:
        contacts.append(f"{matricula} {nome} <{nascimento}>")

        print("\n".join(contacts))

try:

    conn = mariadb.connect(
        user="root",
        password="Javeio2023*",
        host="localhost",
        port=3306)

    cur = conn.cursor()
    conn.close()
    print("s")

except mariadb.Error as e:
      print(f"Error connecting to MariaDB Enterprise: {e}")
      sys.exit(1)

def execute(self, cur):
    pass
