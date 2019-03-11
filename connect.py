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

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `username` (`username`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, (us, ps))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `username` WHERE `username`=%s"
        cursor.execute(sql, ('fadliselaz',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
