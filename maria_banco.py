# Module Import
import mariadb
import sys


# Print List of Contacts
def imprime(self):

     contacts = []

     self.execute( "SELECT matricula, nome, idade FROM mysql.cadastrar_aluno", )

     for (matricula, nome, idade) in self:
        contacts.append(f"{matricula} {nome} <{idade}>")

     print("\n".join(contacts))


