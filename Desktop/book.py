from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {
        'id':1,
        'book_name':'The Hobbit',
        'author': 'J.R.R. Tolkein',
        'publisher': 'Houghton Mifflin Harcourt'
    }
    {
        'id':2,
        'book_name':'The Hunger Games',
        'author':'Suzanne Collins',
        'publisher':'Scholastic'
    }
]

@app.route('/books',methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id', methods=['GET'])
def get_book(id):
    book = [book for book in books if book['id']==id]
    book[0]['book_name'] = request.json.get('book_name',book[0]['book_name'])
    book[0]['author']= request.json.get('publisher',book[0]['publisher'])
    return jsonify(book[0])

@app.route('/books/<int:id>',methods=['DELETE'])
def delete_book(id):
    book = [book for book in books if book['id']==id]
    books.remove(book[0])
    return jsonify({'result':'Book deleted'})
