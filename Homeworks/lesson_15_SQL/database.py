import mysql.connector as mysql

connection = mysql.connect( 
      user = 'root', 
      passwd = 'PassForData12345',
      host = 'localhost',
      port = 3306,
      database = 'testing_database' 
)

cursor = connection.cursor()