# декораторы - делаем код красивее 
# def calc():
#     print(1 + 1)
# # print(calc)
# new_calc = calc # перезаписали саму функцию в другое имя переменной 
# new_calc()

# def greet():
    
#     def hello():
#         return 'hello'
#     return hello()
# # print(greet())

# def outer():
#    """
#    testing 
   
#    возвращает вложенную функцию inner 
#    """
#     def inner():
#         result = 2 + 5
#         return result 
#     return inner # возвращаем всю функцию 

# inner_function = outer()
# print(inner_function())

# def func1(give_me_a_func): 
#     print('before')
#     give_me_a_func()
#     print('after')

# def simple1():
#     print('simple1')

# def simple2():
#     print('simpe2')

# func1(simple1)

# def add_text(func):
#     def wrapper():
#         print('before')
#         func()
#         print('after')
#     return wrapper


# def simple1():
#     print('simple1')

# simple1()

# simple1 = add_text(simple1)
# print(simple1)

# simple1()

# def simple2():
#     print('simple2')

# simple2()

# simple2 = add_text(simple2)

# simple2()


# def add_text(func):
#     def wrapper():
#         print('before')
#         func()
#         print('after')
#     return wrapper

# @add_text # декоратор - он вызывает add_text(simple1)()
# def simple1():
#     print('simple1')

# @add_text
# def simple2():
#     print('simple2')

# simple1()
# simple2()

# def add_logs(func): # функция логов - прикольная штука 
    
#     def wrapper():
#         print(f'function {func.__name__} started') # вызываем имя функции через __name__
#         result =  func()
#         print(f'finished {func.__name__}')
#     return wrapper

# @add_logs
# def simple112():
#     print('simple1')
# simple112()

# @add_logs
# def simple2():
#     print('simple2')


# def add_logs(func):
    
#     def wrapper(*args):
#         print(f'function {func.__name__} started') 
#         result =  func(*args)
#         print(f'finished {func.__name__}')
#     return wrapper

# @add_logs
# def calc(x):
#     print(x * 3)
# calc(4)

# @add_logs
# def calc2(x, y):
#     print(x * y)
# calc2(5, 100)
 

# def func_test(*args): # передали кортеж со значениями
#     print(args) # просто распечатали переданный кортеж
#     print(*args) # распакрвали кортеж и скормили элементы из него (можно использовать как распаковку) 

# func_test(1, 4, 5, 7)


# # list comprehension - генератор списков 
# first_list = [1, 2, 5, 6, 7, 8, 10]

# # second_list = [] # не лучший вариант, быстрее будет вариант с for в одну строку (1 вариант) 
# # for x in first_list: 
# #     second_list.append(x * 2)
# # print(second_list)

# second_list = [x * 2 for x in first_list] # средний вариант, лучше будет вариант с map и lambda (2 вариант) 

# # second_list = map(lambda x: x * 2, first_list) # по идее самый лучший и быстрый вариант перебора элементов коллекции (3 вариант)

# # print(list(second_list)) 
# print(second_list)

# first_list = [1, 2, 5, 6, 7, 8, 10] # фильтрация путем list comprehension
# second_list = [x for x in first_list if x % 2 == 0]
# # можно засунуть в list comprehension полную структуру if else + тернарный оператор test_list = [x if x % 2 == 0 else x + 1 for x in first_list] сначала указывем что, потом условие, потом откуда брать данные 
# print(second_list)

 
# first_list = [1, 2, 5, 6, 7, 8, 10]

# first_dict = {} # создаем словарь 
# for x in first_list:
#    first_dict[x] = x * 2 # указываем ключ х до "=", а значение после "="

# print(first_dict)

# first_dict = {x: x * 3 for x in first_list} # ключ указываем до :, значение после : 
# print(first_dict)

data = [{'one', 'two'}, {'three', 'four'}]

new_dict = {}
for key, value in data:
   new_dict[key] = value
print(new_dict)

countries = ['usa', 'russia', 'belarus']
temps = [23, 32, 55]
countries_temps_dict = dict(zip(countries, temps)) # создали один словарь из двух потоков данных
print(list(zip(countries, temps))) # создали лист с 3 кортежами из двух потоков данных 
print(countries_temps_dict)
