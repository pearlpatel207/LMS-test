import sqlite3

def create_db():
    db = sqlite3.connect('LIB')
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS books (BID varchar(256), TITLE varchar(256), AUTHOR varchar(256), STATUS varchar(256))')
    cursor.execute('CREATE TABLE IF NOT EXISTS books_issued (BID varchar(256) , ISSUEDTO varchar(256))')
    db.commit()
    db.close()

create_db()