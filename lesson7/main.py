import sqlite3

conn = sqlite3.connect('lesson_7.db')
cursor = conn.cursor()

login = input("enter the login")
password = input("enter the pass")

sql = "INSERT INTO user (login, password) VALUES(?, ?)"
query_response = cursor.execute(sql, [login, password])
conn.commit()


conn.close()