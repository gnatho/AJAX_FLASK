from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3 as sql
import json


app = Flask(__name__)


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

    return render_template("list.html", rows=rows)

@app.route('/s')
def s():
    navigation = []
    with open('test.json', 'r') as f:
        d = json.load(f)
        f.close()

    for page in d['storyContent']:
        navigation.append(page['sentences'])

    title = 'Menel i spolka'
    return render_template("story_demo.html", navigation=navigation, title=title, d=d)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


