import mysql.connector as mariadb

try:
    conn = mariadb.connect(
        user = "testUser",
        password = "Passwd123!",
        host = "192.168.188.26",
        database = "testdb",
        port = 3307
    )

    cur = conn.cursor()
    cur.execute("insert into testTable1 (Column1) Values (""Test Python"")")
    #cur.execute("select * from testTable1")

    #for (Column1, Column2) in cur:
    #    print(f" {Column1} {Column2}")
except mariadb.Error as e:
    print(f"Error: {e}")
