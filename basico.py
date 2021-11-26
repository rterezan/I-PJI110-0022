# Module Import
import mariadb
import sys

# Gravar dados
def add_contact(cur, nov_matric, nov_nome, nov_cpf, nov_endereco):

    cur.execute("INSERT INTO mysql.teste_db(matricula, nome, cpf, endereco) VALUES (?, ?, ?, ?)",(nov_matric, nov_nome, nov_cpf, nov_endereco))

try:
   conn = mariadb.connect(
     user="root",
        password="Javeio2023*",
        host="localhost",
        port=3306,
        autocommit=True)

   # Instanciar Cursor
   cur = conn.cursor()

   # Initialize Data to add a single contact
   nov_matric = input("Matrícula")
   nov_nome = input("Nome")
   nov_cpf = input("CPF")
   nov_endereco = input("Endereço")

   # Call function to add a single contact
   add_contact(cur,
       nov_matric,
       nov_nome,
       nov_cpf,
       nov_endereco)

   conn.close()

except mariadb.Error as e:
       print(f"Error connecting to MariaDB Enterprise, or running DML : {e}")
       sys.exit(1)
