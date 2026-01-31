import mariadb

con = mariadb.connect(
    user='testUser',
    host= '192.168.188.26',
    database = 'testdb',
    passwd = 'Passwd123!',
    port = 3307
)

mycursor = con.cursor()

mycursor.execute("SHOW DATABASES;")
for i in mycursor:
    print(i)

con.commit()