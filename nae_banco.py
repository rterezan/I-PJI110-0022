# Module Import
import mariadb
import sys

# Instantiate Connection
try:
   conn = mariadb.connect(
      user="root",
      password="Javeio2023*",
      host="localhost",
      port=3306)

   print("sim")

   # Use Connection

   # Close Connection
   conn.close()

except mariadb.Error as e:
   print(f"Error connecting to MariaDB Enterprise: {e}")
   sys.exit(1)

