import sqlite3 as sq

connection = sq.connect("workouts.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE WORKOUT (exercise text, set int, reps int, weight int, date text)")

connection.close()