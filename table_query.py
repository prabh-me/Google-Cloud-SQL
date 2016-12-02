import pymysql.cursors

connection = pymysql.connect(host='X.Y.Z.W', user='root', password='XXXXXXX', db='XXXXXXXX', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Query an existing table
        sql = "select * from users"
        cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes. (If you made some)
        connection.commit()

finally:
    connection.close()
