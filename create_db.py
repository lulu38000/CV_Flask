import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO clients (nom, prenom, message) VALUES (?, ?, ?)",('DUPONT', 'Emilie', '123, bonjour'))
cur.execute("INSERT INTO clients (nom, prenom, message) VALUES (?, ?, ?)",('LEROUX', 'Lucas', 'salut'))
cur.execute("INSERT INTO clients (nom, prenom, message) VALUES (?, ?, ?)",('MARTIN', 'Amandine', 'oui'))
cur.execute("INSERT INTO clients (nom, prenom, message) VALUES (?, ?, ?)",('TRAMBLEY', 'Antoine', 'non'))
cur.execute("INSERT INTO clients (nom, prenom, message) VALUES (?, ?, ?)",('LAMBERT', 'Sarah', 'ca va'))
cur.execute("INSERT INTO clients (nom, prenom, message) VALUES (?, ?, ?)",('GAGON', 'Nicolas', 'bonsoir'))
cur.execute("INSERT INTO clients (nom, prenom, message) VALUES (?, ?, ?)",('DUBOIS', 'Charlotte', 'salut'))
cur.execute("INSERT INTO clients (nom, prenom, message) VALUES (?, ?, ?)",('LEFEVRE', 'Thomas', 'oui'))


connection.commit()
connection.close()
