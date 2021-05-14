from flask import Flask, render_template, jsonify, request
from queries import *
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/index.html', methods =["GET", "POST"])
def home():
    return render_template('./index.html')

@app.route('/view.html', methods =["GET"])
def view():
    return render_template('./view.html')

@app.route('/addb.html', methods =["GET", "POST"])
def addb():
    return render_template('./addb.html')

@app.route('/deletebook.html', methods =["GET", "POST"])
def deletebook():
    return render_template('./deletebook.html')

@app.route('/issuebook.html', methods =["GET", "POST"])
def issuebook():
    return render_template('./issuebook.html')

@app.route('/returnbook.html', methods =["GET", "POST"])
def returnbook():
    return render_template('./returnbook.html')

@app.route('/addbook',  methods =["POST"])
def addbook():

    bid = request.form['bid']
    title = request.form['title']
    author = request.form['author']
    status = request.form['status']
    
    print(bid,title)
    m = addBook(bid, title, author, status)

    return render_template('./addb.html')

@app.route('/delete/book',  methods =["POST"])
def delbook():
    bid = request.form['bid']
    print(bid)
    m = deleteBook(bid)
    response = 'YAY'
    return jsonify(response), 200

@app.route('/issue/book',  methods =["POST"])
def issbook():
    bid = request.form['bid']
    issueto = request.form['iname']
    print(bid)
    m = issue(bid, issueto)
    response = 'YAY'
    return jsonify(response), 200

@app.route('/return/book',  methods =["POST"])
def rebook():
    bid = request.form['bid']
    print(bid)
    m = returnBook(bid)
    response = 'YAY'
    return jsonify(response), 200

@app.route('/viewB',  methods =["GET"])
def viewB():
    l = viewBooks()
    q = json.dumps(l)
    response = {
        'b': l,
        'leng': len(l)
    }
    return jsonify(response), 200

if __name__ == '__main__':
  app.run()