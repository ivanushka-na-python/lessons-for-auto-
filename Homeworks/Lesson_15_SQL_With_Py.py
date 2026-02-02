import mysql.connector as mysql
# import requests
# fetchall - достает кортежи в списке [{},{}] т.к. он не знает сколько значений достанется, даже если будет только одно 
# fetchone - достает только один кортеж потому что просим достать только 1 кортеж 
# курсор хранит данные только последнего запроса, все прошлые перетираются, если не сохранаять их отдельно

# инъекция name Nastya'; --  т.е. основной прикол мы заходим и комментим вторую часть sql скрипта и можно в сам скрипт засунуть дополнительный запрос как напмример дропнуть все таблицы в бд или саму бд 
# "hacker', 'hacker@evil.com'); DROP TABLE users; --"


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

# db.close()


# ------------------------------------------------------------------------------------------

# cursor = db.cursor(dictionary=True) # более читаемый вариант что мы достаем из бд, обращаясь по ключу доставая значение

# cursor.execute('SELECT * FROM name;') 
# response = cursor.fetchall() 
# for human in response:
#    print(human['surname'])

# db.close()


# ------------------------------------------------------------------------------------------

# cursor = db.cursor(dictionary=True)

# # cursor.execute("select * from name where surname = 'Koterno';") # используем кавычки для показа что котерно это строка, одинаковые кавычки два раза нельзя использовать 
# # response = cursor.fetchall() # достаем столько значений, сколько попадает под сортировку по столбцу фамилии 
# # print(response)

# cursor.execute("select * from name where id = 1;") # 
# response = cursor.fetchone() # достаем только одно значение 
# print(response)

# db.close()
# ------------------------------------------------------------------------------------------

# cursor = db.cursor()

# # query = "select * from people where name = '{0}' and surname = '{1}'" # пидорский нечитаемый код с курса по питону через format 
# # cursor.execute(query.format(input('name').strip(), input('surname').strip()))
# # print(cursor.fetchone())

# db.close()

# ------------------------------------------------------------------------------------------
# cursor = db.cursor()

# name = input('name ').strip() # пацанский код нормальны через f-string
# surname = input('surname ').strip()
# query = f"select * from people where name = '{name}' and surname = '{surname}'"
# cursor.execute(query)
# print(cursor.fetchone())


# db.close()
# ------------------------------------------------------------------------------------------

# cursor = db.cursor() # защищенный от инъекции пацанский код 

# name = input('name ').strip()
# surname = input('surname ').strip()
# query = "select * from people where name = %s and surname = %s;"
# cursor.execute(query, (name, surname))
# print(cursor.fetchall())

# db.close()

# ------------------------------------------------------------------------------------------

# cursor = db.cursor() # инсертаем в таблицу данные, для инсерта нужно коммитнуть обязательно 

# name = input('name ').strip()
# surname = input('surname ').strip()
# query = "insert into people (name, surname) values (%s, %s)"
# cursor.execute(query, (name, surname))
# db.commit()
# print(f'Добавлено строк{cursor.rowcount}') # выводим количество добавленных строк  
# print(f'Id новой записи{cursor.lastrowid}') # выводим id последней добавленной записи 

# db.close()

# # ------------------------------------------------------------------------------------------

# cursor = db.cursor() # выводим по последнему id кортеж, который только добавили 

# name = input('name ').strip()
# surname = input('surname ').strip()
# query = "insert into people (name, surname) values (%s, %s)"
# cursor.execute(query, (name, surname))
# db.commit()
# people_id = cursor.lastrowid
# cursor.execute(f"select * from people where id = {people_id}")
# print(cursor.fetchone())

# db.close()

# ------------------------------------------------------------------------------------------

cursor = db.cursor() # при множественной вставке лучше использовать список кортежей 

values = [
   ('Sasha', 'Dub'),
   ('Sasha', 'Dubik'), 
   ('Ivan ','Morenko')
]
query = "insert into people (name, surname) values (%s, %s)"
cursor.executemany(query, values) # множественная вставка/множественное выполнение 
db.commit()
print(f'Добавлено строк{cursor.rowcount}') # выводим количество добавленных строк  
print(f'Id новой записи{cursor.lastrowid}') # выведится только последний id записи из пакета 

db.close()

# ------------------------------------------------------------------------------------------


# приколюхи питона match case и walrus 
