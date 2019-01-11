from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3 as sql
import mysql.connector
import json
import os

isWin = False
db_host_address = 'gnatho.mysql.pythonanywhere-services.com'
db_name = 'gnatho$content'

if os.getenv('OS') == 'Windows_NT':
    isWin = True
    db_host_address = '127.0.0.1'
    db_name = 'content'


app = Flask(__name__)


@app.route('/story/<string:book_id>/<int:story_id>')   #int has been used as a filter that only integer will be passed in the url otherwise it will give a 404 error
def find_question(book_id, story_id):
    return ('you asked for question {0} {1}'.format(book_id, story_id))

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/_get_data')
def get_data():
    f = open('source.txt', 'r')
    r = f.read()
    f.close()
    return jsonify(result=r)

@app.route('/_balony')
def balony():



        try:

            city = request.args.get('city')
            if city == '':
                return jsonify(result="error")


            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO students (city) VALUES('"+city+"')")

                con.commit()
                print("Record successfully added")
        except:
            con.rollback()
            print("error in insert operation")

        finally:
            return render_template("index.html")
            con.close()


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall();
    con.close()

    return render_template("list.html", rows=rows)

@app.route('/s')
def s():
    with open('test.json', 'r') as f:
        d = json.load(f)
        f.close()
        l = [1, 2, 3, 4, 5, 6, 7, 10]
    return render_template("story_demo.html", d=d, seq=l)

@app.route('/l/<lvl>')
def l(lvl):

    con = mysql.connector.connect(user='gnatho', password='content69',
                                host=db_host_address, database=db_name,
                                auth_plugin='mysql_native_password')

    # con = sql.connect("books.db")

    con.row_factory = sql.Row

    cur = con.cursor()

    query_string = '''SELECT bookId FROM books WHERE level = %s AND mp3path IS NOT NULL'''
    cur.execute(query_string, (lvl,))

    # stare ustawienia
    # query_string = "SELECT bookId FROM books WHERE level = ? AND mp3path NOT NULL"
    # cur.execute(query_string, (lvl,))

    rows = cur.fetchall()
    con.close()
    books = []
    for row in rows:
        books.append(row[0])

    return render_template("l.html", books=books, lvl=lvl)



@app.route('/t/<storyId>')
def t(storyId):

    return render_template("t.html", storyId=storyId)

@app.route('/slider/<bookid>')
def slider(bookid):
    con = mysql.connector.connect(user='gnatho', password='content69',
                                  host=db_host_address, database=db_name,
                                  auth_plugin='mysql_native_password')
    con.row_factory = sql.Row
    cur = con.cursor()
    query_string = "SELECT title, numpages  FROM books WHERE bookid = %s"
    cur.execute(query_string, (bookid,))

    row = cur.fetchone()
    con.close()

    return render_template("slider.html", bookId=bookid, title=row[0], numpages=int(row[1]), isWin=isWin)

@app.route('/quiz/<bookid>')
def quiz(bookid):
    con = mysql.connector.connect(user='gnatho', password='content69',
                                  host=db_host_address, database=db_name,
                                  auth_plugin='mysql_native_password')
    con.row_factory = sql.Row
    cur = con.cursor()
    query_string = "SELECT mp3files FROM books WHERE bookid = %s"
    cur.execute(query_string, (bookid,))

    row = cur.fetchone()[0]
    row = row.split(',')
    row = [int(i) for i in row]
    con.close()
    return render_template("quiz.html", title=bookid, book=row)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


