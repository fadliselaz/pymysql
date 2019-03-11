import pymysql.cursors
import os


#kali ini kita akan mencari username yang ada di dalam data

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='py_database',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

x = str(input("masukan username: "))

with connection.cursor() as cr:
    sql = f"select username from username where username='{x}'"
    cr.execute(sql)
    result = cr.fetchone()
    os.system("cls")

    if result:
        print(f"""
Selamat datang {x}
        """)
    else:
        print(f"{x} tidak ditemukan")

