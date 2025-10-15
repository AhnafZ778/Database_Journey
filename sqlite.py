import sqlite3

connect = sqlite3.connect("test.db")

cursor = connect.cursor()

# sql = """create table cars(
#     ID integer primary key autoincrement,
#     manufacturer text,
#     model text,
#     price integer
#     )"""

sql = "insert into cars (manufacturer, model, price) values('Buggati', 'Chiron', 900000)"

cursor.execute(sql)

connect.commit()

# results  = cursor.fetchall()

# for result in results:
#     print(result[1])