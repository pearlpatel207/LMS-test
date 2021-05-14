import sqlite3
from queries import *

db = sqlite3.connect('LIB')
cursor = db.cursor()

cursor.execute('SELECT * FROM books')
for row in cursor.fetchall():
    print(row)

cursor.execute('SELECT * FROM books_issued')
for row in cursor.fetchall():
    print(row)