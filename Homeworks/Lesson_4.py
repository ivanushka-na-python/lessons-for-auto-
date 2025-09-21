# операторы присваивания 
# "=" просто присваиваем знавение переменной 
# a = 1 
# a = a + 1
#  (a) 

# операторы составного присваивания (+= ; -= ; *= ; /= ; %= ; **= ; //= ; ) (присваивание с арифметическим действием) 
# a = 1 
# a += 1
#  (a)

# a = 5
# a *= 5
# print (a) 
 
# text = "text"
# # text = text + " new"
# text += " new"
# print (text)

# text = "-"
# print (text * 10)

# symbol = "="
# symbol *= 20
# print (symbol)

# операторы принадлежности (in; not in) (в или не в чем-то)
# text = "hello, world, im fine"
# print ("hello" in text)

# # операторы идентичности (is; not is) (объект идентичен другому объекту полностью)
# first_number = 255
# print (255 is first_number)

# second_number = 100
# # print (id (second_number))
# a = 500 
# b = 500
# print (a is b)

#способы ввода данных (клава, чтение из файла, бд, api)
# input ("hello")

# user_name = input ("What is your name")
# print ("hello", user_name, "!")

# user_input = input ("Write something")
# print (type(user_input))

# преобразование типов данных ()
# a = "1"
# a = int (a)
# print (type(a))

# user_number = int(input("write a number"))
# print (type(user_number))

# базовые типы данных в питоне (number, string, boolean, float) коллекции (list - список, dictionary - словарь, tuple - кортеж, set - множество)
# list - (список) для хранения последовательностей 


# first_list = [1, 3, 5, "hello", 2.45]
# # print (first_list[2])
# отсчет элементов начинается с 0 


# first_list = [1, 3, 5, "hello", 2.45]
# first_list [1] = 42
# print (first_list[1])
# считая с конца, считаем с 1 

# изменяемые и не изменяемые типы данных: базовые типы данных не изменяемы - они перезаписываемые, а коллекции изменяемы 
# my_list = []
# my_list = list ()
# my_list.append(42)
# # добавить в конец
# print (my_list)

# my_list = [34.565, "text", 54, 43]
# print (len(my_list))
# узнать сколько элементов в списке 

# my_list = [34.565, "text", 54, 43]
# print (my_list.index("text"))

# # узнать id элемента 


# my_list = [34.565, "text", 54, 43]
# poped = my_list.pop (0) # удаление элемента из списка
# my_list.pop (0) # запоминаем удаленный элемент из списка
# print (my_list)
# print (poped)

# my_list = [34, 76, 4124, 355]
# print (44 in my_list)

# # tuple - (кортеж)
# my_tuple = (1, 1, 1, 2, 65, "text")
# print (my_tuple.count(1))
# смотрим сколько элементов одинаковых в кортеже/списке 
# если создаем кортеж с одним элеметом - нужно после этого элемента ставить ","

# set - (множество)
# содержит только не повторяющиеся элементы 
# не гарантирует порядок элементов 
# my_set = {1, 2, 3, "text", 2.42}
# my_set.add (42)
# print (my_set)

# my_list = (1, 2, 3, 1, 2, 3)
# my_list = set (my_list)
# print (my_list)
# # достаем только уникальные значения
# my_list = list(set([1, 2, 3, 4, 1, 2]))
# print (my_list)

# # dictionary - (словарь)
# # коллекция произвольных объектов с доступом по ключу, данные : пары ключ - значение
# значеинем может быть любой тип данных, ключом может быть базовый тип данных и кортеж
# my_dict = {"first_key" : 1, "second_key" : 2}
# print (my_dict["first_key"])

# my_dict = {"first_key" : 1, "second_key" : 2}
# my_dict ["third_key"] = 3
# # print (my_dict)
# print (my_dict.keys())
# print (my_dict.values())
# print (my_dict.items())