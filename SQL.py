import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    auth_plugin='mysql_native_password'
)

names = []
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    names.append(x[0])
print(names)

# ---------------------------------------
mycursor = mydb.cursor()

sql = "INSERT INTO products (producent, name, size, parameterI, parameterII) VALUES (%s, %s, %s, %s,%s)"
val = ("Maxbud", "Cegła biała", "20x30", "", "")
mycursor.execute(sql, val)

mydb.commit()
