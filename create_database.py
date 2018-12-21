import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE students (city TEXT)')

conn.close()
