import mysql.connector as mysql
# fetchall - достает кортежи в списке [{},{}] т.к. он не знает сколько значений достанется, даже если будет только одно 
# fetchone - достает только один кортеж потому что просим достать только 1 кортеж 
# курсор хранит данные только последнего запроса, все прошлые перетираются, если не сохранаять их отдельно

# Возвращает объект соединения БД



# cursor = db.cursor() 

# cursor.execute('SELECT * FROM name;') #execute - выполнить 
# response = cursor.fetchall() #fetchall - возвращаем ВСЕ что было на запрос выполнить 
# for i in response: # достаем из бд элементы по индексу колонок (не очень хорошая затея обращаться по индексу)
#       print(i[2])



# cursor = db.cursor(dictionary=True) # более читаемый вариант что мы достаем из бд, обращаясь по ключу доставая значение

# cursor.execute('SELECT * FROM name;') 
# response = cursor.fetchall() 
# for human in response:
#    print(human['surname'])



# cursor = db.cursor(dictionary=True)

# # cursor.execute("select * from name where surname = 'Koterno';") # используем кавычки для показа что котерно это строка, одинаковые кавычки два раза нельзя использовать 
# # response = cursor.fetchall() # достаем столько значений, сколько попадает под сортировку по столбцу фамилии 
# # print(response)

# cursor.execute("select * from name where id = 1;") # 
# response = cursor.fetchone() # достаем только одно значение 
# print(response)

# cursor = db.cursor()

# # query = "select * from people where name = '{0}' and surname = '{1}'"
# # cursor.execute(query.format(input('name').strip(), input('surname').strip()))
# # print(cursor.fetchone())


# name = input('name ').strip()
# surname = input('surname ').strip() # гпт решение вроде как не позволяет sql инъекцию 
# query = f"select * from people where name = '{name}' and surname = '{surname}'"
# cursor.execute(query)
# print(cursor.fetchone())


# db.close()


