from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.app_context().push()
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), unique=True, nullable=False)
    publisher = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.name} - {self.author} - {self.publisher}'


@app.route('/')
def index():
    return 'hello pirince'


@app.route('/books')
def get_books():
    books = Books.query.all()
    output = []
    for book in books:
        book_data = {'name': book.name, 'author': book.author,
                     'publisher': book.publisher}
        output.append(book_data)
    return {'books': output}


@app.route('/books/<id>')
def get_book(id):
    book = Books.query.get_or_404(id)
    return {"name": book.name, "author": book.author, "publisher": book.publisher}


@app.route('/books', methods=['POST'])
def add_book():
    book = Books(
        name=request.json['name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}
