import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY AUTOINCREMENT, category text)"
cursor.execute(create_table)
test = "INSERT INTO categories(category) VALUES('Businnes')"
cursor.execute(test)
test = "INSERT INTO categories(category) VALUES('Health')"
cursor.execute(test)
test = "INSERT INTO categories(category) VALUES('Economic')"
cursor.execute(test)
test = "INSERT INTO categories(category) VALUES('Sport')"
cursor.execute(test)
test = "INSERT INTO categories(category) VALUES('Travel')"
cursor.execute(test)
test = "INSERT INTO categories(category) VALUES('Religion')"
cursor.execute(test)


connection.commit()
connection.close()