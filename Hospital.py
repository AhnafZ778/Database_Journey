import sqlite3
from time import sleep

connect = sqlite3.connect("Hospital_Database.db")

cursor = connect.cursor()

sql_table = """Create table if not exists patients(
        id integer primary key autoincrement,
        name text,
        disease text,
        age integer
)"""
connect.execute(sql_table)
while True:
    print("Do you want to register an appointment?")
    a = int(input("1.Yes 2. No\n-->  "))
    if a == 1:
        name = input("Name of patient?\n-->  ")
        disease = input("Please state the reason for your visit?\n-->  ")
        age = int(input("What is the age of the patient?\n-->  "))
        print("Please wait while we register you into the registry\n-->  ")
        print("Wait..", end = "")
        for i in range(5):
            print(".", end = "")
            sleep(0.1)
        sql = f"insert into patients (name, disease, age) values('{name}','{disease}',{age})"
        connect.execute(sql)
        print("\nPatient has been successfully registered")
    elif a == 2:
        break
    else:
        print("Please input a valid response")
        




connect.commit()
