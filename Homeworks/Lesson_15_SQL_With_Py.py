import mysql.connector as mysql
import requests
# fetchall - достает кортежи в списке [{},{}] т.к. он не знает сколько значений достанется, даже если будет только одно 
# fetchone - достает только один кортеж потому что просим достать только 1 кортеж 
# курсор хранит данные только последнего запроса, все прошлые перетираются, если не сохранаять их отдельно

# Возвращает объект соединения БД

db = mysql.connect( 
      user = 'root', 
      passwd = 'PassForData12345',
      host = 'localhost',
      port = 3306,
      database = 'testing_database' 
)

# cursor = db.cursor() 

# cursor.execute('SELECT * FROM name;') #execute - выполнить 
# response = cursor.fetchall() #fetchall - возвращаем ВСЕ что было на запрос выполнить 
# for i in response: # достаем из бд элементы по индексу колонок (не очень хорошая затея обращаться по индексу)
#       print(i[2])

# ------------------------------------------------------------------------------------------

# cursor = db.cursor(dictionary=True) # более читаемый вариант что мы достаем из бд, обращаясь по ключу доставая значение

# cursor.execute('SELECT * FROM name;') 
# response = cursor.fetchall() 
# for human in response:
#    print(human['surname'])

# ------------------------------------------------------------------------------------------

# cursor = db.cursor(dictionary=True)

# # cursor.execute("select * from name where surname = 'Koterno';") # используем кавычки для показа что котерно это строка, одинаковые кавычки два раза нельзя использовать 
# # response = cursor.fetchall() # достаем столько значений, сколько попадает под сортировку по столбцу фамилии 
# # print(response)

# cursor.execute("select * from name where id = 1;") # 
# response = cursor.fetchone() # достаем только одно значение 
# print(response)

# ------------------------------------------------------------------------------------------

# cursor = db.cursor()

# # query = "select * from people where name = '{0}' and surname = '{1}'" # пидорский нечитаемый код с курса по питону через format 
# # cursor.execute(query.format(input('name').strip(), input('surname').strip()))
# # print(cursor.fetchone())


# ------------------------------------------------------------------------------------------
# cursor = db.cursor()

# name = input('name ').strip() # пацанский код нормальны через f-string
# surname = input('surname ').strip()
# query = f"select * from people where name = '{name}' and surname = '{surname}'"
# cursor.execute(query)
# print(cursor.fetchone())


# db.close()
# ------------------------------------------------------------------------------------------

cursor = db.cursor() # защищенный от инъекции код 

query = "select * from people where surname = %s and name = %s"
name = input('name ').strip
surname = input('surname ').strip
cursor.execute(query, (surname, name))
print(cursor.fetchall())

db.close()

# ------------------------------------------------------------------------------------------

