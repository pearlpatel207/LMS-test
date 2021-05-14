import sqlite3
from flask import jsonify

db = sqlite3.connect('LIB')
cursor = db.cursor()

def addBook(bid, title, author, status):
    db = sqlite3.connect('LIB')
    cursor = db.cursor()

    try:
        cursor.execute('INSERT INTO books VALUES (?,?,?,?)', [bid, title, author, status])
        message = 'Success', "Book added successfully"

    except:
        message = 'Error', "Can't add data into Database"

    db.commit()
    db.close()

    return jsonify(message)


def deleteBook(bid):
    db = sqlite3.connect('LIB')
    cursor = db.cursor()
    try:
        cursor.execute('DELETE FROM books WHERE bid=(?)', [bid])
        cursor.execute('DELETE FROM books_issued WHERE bid=(?)', [bid])
        message = 'Success', "Book Record Deleted Successfully"
    except:
        message = 'Error', "Please check Book ID"

    db.commit()
    db.close()
    return jsonify(message)

def issue(bid, issueto):
    db = sqlite3.connect('LIB')
    cursor = db.cursor()

    allBid = []
    try:
        cursor.execute('SELECT bid FROM books')
        for row in cursor.fetchall():
            allBid.append(row[0])

        if bid in allBid:
            
            cursor.execute('SELECT STATUS FROM books WHERE bid = (?)', bid)
            for row in cursor.fetchall():
                check = row[0]

            if check == 'avail':
                status = True
            else:
                status = False
            
        else:
            message = "Error", "Book ID not present"
    except:
        message = "Error", "Can't fetch Book IDs"

    try:
        if status == True:
            print('yes')
            cursor.execute('INSERT INTO books_issued VALUES(?,?)', [bid, issueto])
            cursor.execute('UPDATE books SET STATUS="issued" WHERE bid=(?)', [bid])
            message = 'Success', "Book Issued Successfully"
        else:
            message = 'Message', "Book Already Issued"
    except:
        message = "Search Error", "The value entered is wrong, Try again"

    db.commit()
    db.close()

    print(message)
    return

def viewBooks():
    db = sqlite3.connect('LIB')
    cursor = db.cursor()

    l = []

    try:
        cursor.execute('SELECT * FROM books')
        for i in cursor.fetchall():
            l.append(i)

        db.close()

    except:
        message = 'Error', "Failed to fetch files from database"
    

    return l



def returnBook(bid):
    db = sqlite3.connect('LIB')
    cursor = db.cursor()

    allBid = []

    try:
        cursor.execute('SELECT bid FROM books')
        for row in cursor.fetchall():
            allBid.append(row[0])

        if bid in allBid:
            cursor.execute('SELECT STATUS FROM books WHERE bid = (?)', [bid])
            for row in cursor.fetchall():
                check = row[0]

            if check == 'issued':
                status = True
            else:
                status = False

        else:
            message = "Error", "Book ID not present"
    except:
        message = "Error", "Can't fetch Book IDs"

    try:
        if bid in allBid and status == True:
            cursor.execute('DELETE FROM books_issued WHERE bid=(?)', [bid])
            cursor.execute('UPDATE books SET STATUS="avail" WHERE bid=(?)', [bid])
            message = 'Success', "Book Returned Successfully"


        else:
            allBid.clear()
            message = 'Message', "Please check the book ID"
    except:
        message =  "Search Error", "The value entered is wrong, Try again"

    db.commit()
    db.close()

    return jsonify(message)