import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from sqlalchemy import text

back = Flask(__name__)
conn = back.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bansal31@localhost/BOOK_MANAGEMENT_APP'
db = SQLAlchemy(back)

class BOOKS(db.Model):
    __tabelname__ ='BOOKS'
    ISBN = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(120))
    Author = db.Column(db.String(120))
    Year = db.Column(db.Integer)

    def __init__(self,ISBN, Title, Author, Year):
        self.ISBN = ISBN
        self.Title = Title
        self.Author = Author
        self.Year = Year

# Inserting books details into databse
def insert(title,author,year,isbn):
    new_record = BOOKS(isbn,title,author,year)
    db.session.add(new_record)
    db.session.commit()


def view():
    # fetching all data from postgresql
    Datas = db.session.query(BOOKS).all()

    list_ = []

    for data in  Datas:
        values = []
        Isbn_val = data.ISBN
        Author_val = data.Author
        Title_val = data.Title
        Year_val =  data.Year
        values.append(Isbn_val),values.append(Author_val),values.append(Title_val),values.append(Year_val)
        list_.append(values)
    return  list_
    # print(list_))

def update(title,author,year,isbn):
    # query the database to get the book with the specefied ISBN
    book_ = db.session.query(BOOKS).filter_by(ISBN=isbn).first()
    print([book_.Title, book_.ISBN, book_.Author, book_.Year])
    if book_:
        book_.Title = title
        book_.Author = author
        book_.Year = year
    # Commit the changes to the database
        db.session.commit()
        # print("succesfully")
        # print(book_)

def search(title="",author="",year="",isbn=""):
    result = []

    book_ = BOOKS.metadata.tables["BOOKS"]

    #  create list for filter conditions
    filters = []
    if title:
        filters.append(book_.c.Title == title)
    elif isbn:
        filters.append(book_.c.ISBN == isbn)
    elif author:
        filters.append(book_.c.Author == author)

    if filters:
        query = book_.select().where(or_(*filters))
    else:
        # If no filters provided, select all
        query = book_.select()

    # We iterate through the results and build a list of dictionaries containing book details.

    for instance in db.session.execute(query):
        output = []
        output.append(instance.ISBN), output.append(instance.Author), output.append(instance.Title), output.append(instance.Year)
        result.append(output)
    return result

def delete(title):
   to_be_delete = db.session.query(BOOKS).filter_by(Title=title).first()
   db.session.delete(to_be_delete)
   db.session.commit()
