#!/usr/bin/python3
from flask import Flask, jsonify, request, Response 

app = Flask(__name__)

books = [
        {
            'name' : 'gost town',
            'price' : 12.40,
            'ibn' : 1234
            },
        {
            'name' : '2 worlds',
            'price' : 15.99,
            'ibn' : 4456
            }
        ]

def validObject(bookobj):
    if ( "name" in bookobj and "price" in bookobj and "ibn" in bookobj ):
        return True
    else:
        return False

@app.route('/')
def default():
    return ("Hello World")

@app.route('/books')
def get_book():
    return jsonify({'books' : books})

@app.route('/books/<int:ibn>',methods=['PUT'])
def replace_book(ibn):
    new_data = request.get_json()
    new_book = {
            'name': new_data['name'],
            'price': new_data['price'],
            'ibn': ibn
            }
    i = 0;
    for book in books:
        currentibn = book["ibn"]
        if currentibn == ibn:
            books[i] = new_book
        i += 1
    response = Response("", status=204)
    return (response)

@app.route('/books/<int:ibn>',methods=['PATCH'])
def update_book(ibn):
    new_data = request.get_json()
    response = Response("",status=200)
    if ( 'name' in new_data ):
        i = 0;
        for book in books:
            currentibn = book["ibn"]
            if currentibn == ibn:
                book["name"] = new_data["name"]
                response = Response("update name", status=204 )
            i += 1
        return response
    if ( 'price' in new_data ):
        i = 0;
        for book in books:
            currentibn = book["ibn"]
            if currentibn == ibn:
                book["price"] = new_data["price"]
                response = Response("update price", status=204)
            i += 1
        return response
    return response

@app.route('/books', methods=['POST'])
def put_book():
    data = request.get_json()
    if ( validObject(data) ):
        newBook = {
            "name" : data["name"],
            "price" : data["price"],
            "ibn" : data["ibn"]
            }
        books.insert(0,newBook)
        response = Response("True", 201, mimetype='application/json')
        return response
    else:
        return "False"


@app.route('/books/<int:ibn>')
def get_ibn_book(ibn):
    return_value = {}
    for book in books:
        if book["ibn"] == ibn:
            return_value = {
                    'name' : book["name"],
                    'price' : book["price"]
                    }
    return jsonify(return_value)


app.run(host='0.0.0.0')
