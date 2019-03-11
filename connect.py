import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='py_database',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

us = str(input("masukan username: "))
ps = str(input("masukan password: "))
cari = "fadliselaz"
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = f"INSERT INTO username (username, password) VALUES ('{us}', '{ps}')"
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
    
    with connection.cursor() as cursor:
        # Read a single record
        sql = f"SELECT id, username, password FROM username WHERE username='{us}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
