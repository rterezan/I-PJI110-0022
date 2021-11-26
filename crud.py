import mariadb
import sys

# Adds single contact
def add_contact(cur, first_name, last_name, email):
    """Adds the given contact to the contacts table"""

    cur.execute("INSERT INTO test.contacts(first_name, last_name, email) VALUES (?, ?, ?)",
          (first_name, last_name, email))

# Adds Multiple contacts
def add_multiple_contacts(cur, data):
    """Adds multiple contacts to database from given data"""

    cur.executemany("INSERT INTO test.contacts(first_name, last_name, email) VALUES (?, ?, ?)", data)

# Instantiate Connection
try:
   conn = mariadb.connect(
      user="connpy_test",
      password="passwd",
      host="192.0.2.1",
      port=3306,
      autocommit=True)

   # Instantiate Cursor
   cur = conn.cursor()

   # Initialize Data to add a single contact
   new_contact_fname = "J. R. R."
   new_contact_lname = "Tolkien"
   new_contact_email = "jrr.tolkien@example.edu"

   # Call function to add a single contact
   add_contact(cur,
       new_contact_fname,
       new_contact_lname,
       new_contact_email)

   # Initialize Data to add multiple contacts
   new_contacts = [
       ("Howard", "Lovecraft", "hp.lovecraft@example.net"),
       ("Flannery", "O'Connor", "flan.oconnor@example.com"),
       ("Walker", "Percy", "w.percy@example.edu")
     ]

   # Call function to add multiple contacts
   add_multiple_contacts(cur, new_contacts)

   # Close Connection
   conn.close()

except mariadb.Error as e:
       print(f"Error connecting to MariaDB Enterprise, or running DML : {e}")
       sys.exit(1)
