import mysql.connector as mariadb

def readOutValues():
    try:
        conn = mariadb.connect(
            user = "testUser",
            password = "Passwd123!",
            host = "192.168.188.26",
            database = "testdb",
            port = 3307
        )

        cur = conn.cursor()
        cur.execute("select * from testTable1")

        for (Column1, Column2) in cur:
            print(f" {Column1} {Column2}")
    except mariadb.Error as e:
        print(f"Error: {e}")

def writeValueToDB(entrieValue,entrieValue2):
    try:
        conn = mariadb.connect(
            user = "testUser",
            password = "Passwd123!",
            host = "192.168.188.26",
            database = "testdb",
            port = 3307
        )
        print(entrieValue)
        cur = conn.cursor()
        cur.execute("insert into testTable1 (Column1, Column2) Values (%s, %s)",(entrieValue, entrieValue2))
        conn.commit()
        #cur.execute(f"insert into testTable1 (Column1) Values ('Daniel'))

    except mariadb.Error as e:
        print(f"Error: {e}")
