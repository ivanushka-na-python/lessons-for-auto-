# генераторы 
# def generate_text(text1, text2): # чисто функция 
#    return f'Text consists on the words: {text1} and {text2}'
# print(generate_text('ivan', 'ivanov'))

# # функция-генератор 
# n = 2

# progression = []
# start_num = 1
# while len(progression) < 1000: 
#    progression.append(start_num)
#    start_num += n


# def progression(limit=50):# пока не понял прикола, нужна для работы с большими/бесконечными данными 
#    n = 2
#    start_num = 1
#    count = 1
#    while count < limit:
#       yield start_num
#       start_num += n
#       count += 1
# # print(list(progression()))
# for number in progression():
#    print(number)

# # модули в питоне (библиотеки)
# import random
# # print(random.random())
# print(f'Your price is {int(random.random() * 1000)}') # рандомная цена 

# print(random.randint(0, 10)) # включительно выпадают оба числа 
# print(random.randrange(0, 10)) # не включительно до, т.е. 10 никогда не выпадет 

# users = ['user_1', 'user_2', 'user_3']
# print(random.choice(users))


# import sys
# print(sys.platform)
# # модуль - файл или папка в питоне 

import helper 
helper.assist()


from helper import assist as useful
helper.useful()

from random import random, randrange, choice # прямой импорт
