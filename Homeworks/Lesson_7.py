# еще один цикл while loop 
# i = 0 
# while i < 5: # когда возвращает правду - работает, пока не возвратит ложь 
#    print('hello')
#    i += 1
# else:
#    print('the end')

# while True: # постоянный цикл (прикольная постоянная программа, которая постоянно отслеживает ввод)
#    user_unput = input('''Сколько лет бокса у Димы? 
#                       для выхода - Выход''')
#    user_unput = user_unput.lower()
#    if user_unput == 'выход':
#       user_unput.ex
#    elif user_unput != int:
#       print('только целые числа')
#    elif(int(user_unput)) == 0:
#       print('Правильно, это всем известно')
#    else:
#       print('Ты че, не может быть столько, это же Дима')


# while True: # постоянный цикл (прикольная постоянная программа, которая постоянно отслеживает ввод)
#    user_input = input('Сколько лет бокса у Димы? ')
#    user_input = user_input.lower()
#    if user_input == 'выход':
#       break
#    elif(int(user_input)) == 0:
#       print('Правильно, это всем известно')
#    else:
#       print('Ты че, не может быть столько, это же Дима')


# while True: # постоянный цикл (прикольная постоянная программа, которая постоянно отслеживает ввод)
#    user_input = input('Сколько лет бокса у Димы? ')
#    user_input = user_input.lower()
#    if user_input == 'выход':
#       break
#    elif user_input == 'skip':
#       continue # пропуск шага, код ниже не будет выполняться 
#    elif(int(user_input)) == 0:
#       print('Правильно, это всем известно')
#    else:
#       print('Ты че, не может быть столько, это же Дима')

# text = 'Привет, как дела, я люблю пить пиво'
# words = text.split()
# find_words = []
# for word in words:
#    if 'а' in word:  
#       # print(word)
#       continue
#    find_words.append(word)
# print(' '.join(find_words))

# функции - основные программные структуры, могут принимать аргументы и возвращать результаты выполнения 
# dry -  dont repeat yourself 
# a = 1
# b = 2
# c = 3
# d = 4
# y = 1 
# main_number = 47 
# def calc(numb):
#    if y == 0: 
#       print(numb) 
#    else:
#       print(a + main_number)
# calc(b)


# a = 1
# b = 2
# c = 3
# d = 4
# y = 0 
# main_number = 47 
# def calc(numb):
#    if y == 0: 
#       return numb 
#    else:
#       result = numb + main_number
#       return result 
# calc(b)
# вызов функции def должно идти после описания самой функции, потому что питон идет сверху вниз и запоминает была ли до вызова описана функция 
# у функции print нет return, точне он возвращает none 

# def some_print(first, second, third, fourth, fiveth): # тут параметры 
#    print(f'first word is {first}, second word is {second}, {third}, {fourth}, {fiveth}')
# some_print(first='one', second='two', third='three', fourth='four', fiveth='five') тут аргументы, использование именованных аргументов
# some_print('one', 'two', 'three', 'four', 'five') # позиционные аргументы 

# def power(number, degree=2): #функция возвдит в ту степень, которую ей привязали через = 
#    return number ** degree
# print(power(3, 3)) # для второго параметра, если не указывать значение аргумента берется дефолиное значение, которое уже записано в параметре, 
# если указать, возьмется новое значение переданное в аргумент 

# после именновоного аргумента нужно указывать только именнованные аргументы, на позиционные питон будет ругаться 
# def sum_num(*args): #сколько угодно позиционных параметров могу передавать после * 
#    # result = 0 
#    # for numbs in args:
#    #    result += numbs
#    # return result # изобрел велосипед
#    return sum(args) # залупа какая-то 
# print(sum_num(8, 5, 34))

# def price_list(title, price):
#    print(f'Product {title}, price {price}')
# price_list('iphone', 1500)

# def price_list(**kwargs): # сколько угодно именованных параметров
#    for title, price  in kwargs.items():
#       print(f'Product {title}, price {price}')
# price_list(iphone=1500, laptop=3000, port=6666)

