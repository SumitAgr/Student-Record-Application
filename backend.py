import sqlite3

def connect():
    sql_connect = sqlite3.connect("students.db")
    mouse_cursor = sql_connect.cursor()
    mouse_cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, major TEXT, age INTEGER, sex TEXT, address TEXT, gpa INTEGER")
    sql_connect.commit()
    sql_connect.close()

def insert():
    sql_connect = sqlite3.connect("students.db")
    mouse_cursor = sql_connect.cursor()
    mouse_cursor.execute("INSERT INTO students VALUES (NULL, ?, ?, ?, ?, ?, ?)",(name, major, age, sex, address, gpa))
    sql_connect.commit()
    sql_connect.close()

def view():
    sql_connect = sqlite3.connect("students.db")
    mouse_cursor = sql_connect.cursor()
    mouse_cursor.execute("SELECT * FROM students")
    rows = mouse_cursor.fetchall()
    sql_connect.close()
    return rows

def search(name = "", major = "", age = "", sex = "", address = "", gpa = ""):
    sql_connect = sqlite3.connect("students.db")
    mouse_cursor = sql_connect.cursor()
    mouse_cursor.execute("SELECT * FROM students WHERE name = ? OR major = ? OR age = ? OR sex = ? OR address = ? OR gpa = ?", (name, major, age, sex, address, gpa))
    rows = mouse_cursor.fetchall()
    sql_connect.close()
    return rows

def delete(id):
    sql_connect = sqlite3.connect("students.db")
    mouse_cursor = sql_connect.cursor()
    mouse_cursor.execute("DELETE from students WHERE id = ?", (id, ))
    sql_connect.close()
    return rows

def update(id, name, major, age, sex, address, gpa):
    sql_connect = sqlite3.connect("students.db")
    mouse_cursor = sql_connect.cursor()
    mouse_cursor.execute("UPDATE students SET name = ?, major = ?, age = ?, sex = ?, address = ?, gpa = ?", (name, major, age, sex, address, gpa))
    sql_connect.commit()
    sql_connect.close()

connect()
