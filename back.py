import sqlite3

def connect():
    conn=sqlite3.connect("booss.db")
    cur=conn.cursor()
    cur.execute(" CREATE TABLE IF NOT EXISTS  boos (title text,author text,year integer, isbn integer)")
    conn.commit()
    conn.close()


def insert(title,author,year,isbn):
    conn=sqlite3.connect("booss.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO boos VALUES(?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("booss.db")
    cur=conn.cursor()
    cur.execute("SELECT*FROM boos")
    rows=cur.fetchall()
    conn.close()
    return rows


def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("booss.db")
    cur=conn.cursor()
    cur.execute("SELECT*FROM boos WHERE title=? OR author=? OR year=? OR isbn=? ",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(title):
    conn=sqlite3.connect("booss.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM boos WHERE title=?",(title,))
    conn.commit()
    conn.close()

def update(title,author,year,isbn):
    conn=sqlite3.connect("booss.db")
    cur=conn.cursor()
    cur.execute("UPDATE boos SET title=?,author=?,year=? WHERE isbn=?",( title,author,year,isbn))
    conn.commit()
    conn.close()

connect()
print(search(title="holy"))
print(view())
