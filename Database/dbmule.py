#################

# NJC’s flagship Internship program

#################

import mysql.connector


#Connect to the SQLite database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="database"   # we can connect to server without DB name simply do not mention
)
mycursor = mydb.cursor()


#Creating a new SQLite database 
mycursor.execute("CREATE DATABASE database")


#Creating a new table movies
mycursor.execute("CREATE TABLE movies (id INT AUTO_INCREMENT PRIMARY KEY, actor VARCHAR(255), actress VARCHAR(255), year_of_release int, name VARCHAR(255), director VARCHAR(255))")


#Inserting data into Movies table
sql = "INSERT INTO movies (actor, actress, year_of_release, name, director) VALUES (%s, %s, %s, %s, %s)"
val = [
    ('DiCaprio', 'Kate Winslet',1997,'Titanic','James Cameron'),
    ('DiCaprio', 'Claire Danes',1996,'Romeo and juliet','Baz Luhrmann'),
    ('DiCaprio', 'Emily Mortimer',2010,'Shutter Island','Martin Scorsese'),
    ('DiCaprio', 'Marion Cotillard',2010,'Inception','Chris Nolan'),
    ('Matthew McConaughey', 'Anne Hathaway',2014,'Interstellar','Chris Nolan')
    ]
#mycursor.execute(sql,val) can also be done only if we have one statement to insert
mycursor.executemany(sql, val)
mydb.commit()


#Querying data from Movies table
sql = "SELECT * FROM data"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


#Querying data from Movies table fro a given actor name
sql = "SELECT * FROM data WHERE actor ='DiCaprio'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)