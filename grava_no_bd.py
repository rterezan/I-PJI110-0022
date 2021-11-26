import mariadb
import sys

try:
    conn = mariadb.connect(
        user="root",
        password="Javeio2023*",
        host="localhost",
        port=3306,
        autocommit=True)
        #print("oba")

    # Instanciar Cursor
    cur = conn.cursor()
    nov_matric = reg_aluno.get()
    nov_nome = entra.get()
    nov_cpf = mostra_cpf.get()
    nov_endereco = tender.get()

    self.grava(cur,
            nov_matric,
            nov_nome,
            nov_cpf,
            nov_endereco)

    conn.close()

except mariadb.Error as e:
    print(f"Erro de conexão com o db ou DMLL : {e}")
    sys.exit(1)
