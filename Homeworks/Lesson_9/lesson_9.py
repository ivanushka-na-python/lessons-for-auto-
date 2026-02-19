# summer = True 
# if True: # else не будет выполняться, потому что всегда возвращается true 
#    print('the weather is fine')
# else:
#    print('the weather is not fine')

# summer = True 
# if summer: # всегда будет выполнятся только первое условие, потому что summer всегда true 
#    print('the weather is fine')
# else:
#    print('the weather is not fine')

# a = 'privet kak dela' # распечатает потому что любая не пустая строка это правда 
# # для чисел все что не 0 - правда, для колекций - если есть элемент - правда, если нет - ложь 
# # none - это ложь 
# if a: 
#    print('True')

# # встроенные функции 
# my_list = [1, 7, 12, 9, 5, 10, 54]
# # print(max(my_list)) # максимальное значение в коллекции 
# # print(min(my_list)) # минимальное значение в коллекции 
# # print(sum(my_list)) # сумма всех чисел в коллекции 

# # test_number = 2 / 3
# # print(round(test_number, 1)) # округляет до числа перданного при вызове функции после имени переменной 

# # print(abs(-1)) # возвращает модуль числа 

# print(sorted(my_list)) # сортирует список от меньшего к большему 
# print(sorted(my_list, reverse=True)) # сортирует список в обратном порядке 
# my_list.sort() # отсортировкли коллекцию и сохранили в имя переменной 

# map - применение операции к каждому элементу 
# my_list = [1, 7, 12, 9, 5, 10, 54]
# # def mult_by_2(x):
# #    return x * 2
# # new_list = map(mult_by_2, my_list)
# # print(list(new_list))

# # # lamda - лямда функция (функция, которая помещается в одну строку)
# # my_list = [1, 7, 12, 9, 5, 10, 54]
# # new_list = map(lambda x: x * 2, my_list)
# # print(list(new_list))

# b = 1 if len(my_list) > 20 else 5 # тернарный оператор - используется только с else 
# print(b)

# # filter 
my_list = [1, 7, 12, 9, 5, 10, 54]
def is_even(x):
   if x % 2 == 0:
      return True
   else:
      return False
new_list = filter(is_even, my_list)
print(list(new_list))


# my_list = [1, 7, 12, 9, 5, 10, 54]
# def is_even(x):
#    return x % 2 == 0: # это сравнение, там в любом случае возврат true/false поэтому можно не прописывать return false/true 
# new_list = filter(is_even, my_list)
# print(list(new_list))


# my_list = [1, 7, 12, 9, 5, 10, 54]
# new_list = filter(lambda x: x % 2 == 0, my_list)
# print(list(new_list))

# datetime 
# import datetime
# # time_now = datetime.datetime.now()
# # print(time_now)
# # print(time_now.hour)

# # easy_date = datetime.datetime(1960, 1, 15)
# # print(easy_date)

# my_time = '2023/06/01 12 hours, 30 min, 10 secs'
# python_date = datetime.datetime.strptime(my_time, '%Y/%m/%d %H hours, %M mins, %S secs') # ввод даты для питона 
# print(python_date) # тут ошибка 