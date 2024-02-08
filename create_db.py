import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('DUPONT', 'Emilie', '123, bonjour'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LEROUX', 'Lucas', 'salut'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('MARTIN', 'Amandine', 'oui'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('TRAMBLEY', 'Antoine', 'non'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LAMBERT', 'Sarah', 'ca va'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('GAGON', 'Nicolas', 'bonsoir'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('DUBOIS', 'Charlotte', 'salut'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LEFEVRE', 'Thomas', 'oui'))


connection.commit()
connection.close()
