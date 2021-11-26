# Module Import
import mariadb
import sys

try:
   conn = mariadb.connect(
     user="root",
        password="Javeio2023*",
        host="localhost",
        port=3306,
        autocommit=True)

   # Instanciar Cursor
   cur = conn.cursor()
   print("eba")

except mariadb.Error as e:
       print(f"Error connecting to MariaDB Enterprise, or running DML : {e}")
       sys.exit(1)
