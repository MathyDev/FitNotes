import sqlite3


Create_exercise_table = "Create exercise table(id INTEGER PRIMARY KEY,Exercise TEXT,Bodypart TEXT)"



def connect(): 
    return sqlite3.connect("data.db")

with connection:
    connection.execute(Create_exercise_table)

