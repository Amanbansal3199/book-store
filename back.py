import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

book = Flask(__name__)
conn = book.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bansal31@localhost/BOOK_MANAGEMENT_APP'
db = SQLAlchemy(book)

class BOOKS(db.Model):
    __tabelname__ ='Book'
    ISBN = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(120))
    Author = db.Column(db.String(120))
    Year = db.Column(db.Integer)

    def __init__(self,ISBN, Title, Author, Year):
        self.ISBN = ISBN
        self.Title = Title
        self.Author = Author
        self.Year = Year

def insert(title,author,year,isbn):
    new_record = BOOKS(isbn,title,author,year)
    db.session.add(new_record)
    db.session.commit()


# def connect():
#     conn=sqlite3.connect("booss.db")
#     cur=conn.cursor()
#     cur.execute(" CREATE TABLE IF NOT EXISTS  boos (title text,author text,year integer, isbn integer)")
#     conn.commit()
#     conn.close()
#
#
# def insert(title,author,year,isbn):
#     conn=sqlite3.connect("booss.db")
#     cur=conn.cursor()
#     cur.execute("INSERT INTO boos VALUES(?,?,?,?)",(title,author,year,isbn))
#     conn.commit()
#     conn.close()
#
# def view():
#     conn=sqlite3.connect("booss.db")
#     cur=conn.cursor()
#     cur.execute("SELECT*FROM boos")
#     rows=cur.fetchall()
#     conn.close()
#     return rows
#
#
# def search(title="",author="",year="",isbn=""):
#     conn=sqlite3.connect("booss.db")
#     cur=conn.cursor()
#     cur.execute("SELECT*FROM boos WHERE title=? OR author=? OR year=? OR isbn=? ",(title,author,year,isbn))
#     rows=cur.fetchall()
#     conn.close()
#     return rows
#
# def delete(title):
#     conn=sqlite3.connect("booss.db")
#     cur=conn.cursor()
#     cur.execute("DELETE FROM boos WHERE title=?",(title,))
#     conn.commit()
#     conn.close()
#
# def update(title,author,year,isbn):
#     conn=sqlite3.connect("booss.db")
#     cur=conn.cursor()
#     cur.execute("UPDATE boos SET title=?,author=?,year=? WHERE isbn=?",( title,author,year,isbn))
#     conn.commit()
#     conn.close()
#
# connect()
# print(search(title="holy"))
# print(view())
