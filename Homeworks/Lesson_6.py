# условия 
# user_input = int(input('choose your number: ')) 
# if user_input == 1: 
#    print('One')
# elif user_input == 2:
#    print('Two')
# else: 
#    print('a lot of')

# user_input = (input('choose your number: ')) 
# if user_input.isnumeric(): # функция только для строки 
#    user_input = int(user_input)
#    if user_input == 1: 
#       print('One')
#    elif user_input == 2:
#       print('Two')
#    else: 
#       print('a lot of')
# else:
#    print('Enter a number please')

# циклы 'for' 

# names_list = ['ivan', 'artem', 'nikolai', 'kostya', 'anya']
# for name in names_list:
#    print(name)


# names_list = ['ivan', 'artem', 'nikolai', 'kostya', 'anya', 'ioann', 'inokentiy']
# for name in names_list:
#    if name.startswith('a'):
#       print('Mr', name)
#    else:
#       print(name)


# names_list = ['ivan', 'artem', 'nikolai', 'kostya', 'anya', 'ioann', 'inokentiy']
# for name in names_list:
#    if name.startswith('a'):
#       print('Mr ', end = '') # в конце убираем /n, что бы print не переносил на следующую строку (/n переносит на след строку)
#    print(name.title())

# some_dict = {'tom': 34, 'karl': 54, 'ivan': 12}
# for dict in some_dict:
#    print(dict) # при обычном цикле из словаря достаются только ключи

# some_dict = {'tom': 34, 'karl': 54, 'ivan': 12}
# for dict in some_dict.values(): # достали циклом значения из словаря 
#    print(dict)

# или можно сделать вот так, если надо вытянуть значения из словаря
# some_dict = {'tom': 34, 'karl': 54, 'ivan': 12}
# for dict in some_dict:
#    print(some_dict[dict])

# some_dict = {'tom': 34, 'karl': 54, 'ivan': 12}
# for data in some_dict:
#    print(f'{data}: {some_dict[data]}') # спросить у димы как достаются значения с помname, agощью  {some_dict[data]}

# some_dict = {'tom': 34, 'karl': 54, 'ivan': 12}
# for name, age in some_dict.items(): # говорим чтобы он обращал внимание только на ключ : значения
#    # name, age = data # это не нужно
#    print(f'{name} : {age}')

# text = 'Привет, как дела, я люблю пить пиво'
# words = text.split()
# find_words = []
# for word in words:
#    if 'а' in word:  
#       # print(word)
#       wordless = word
#    else:
#       (find_words.append(word))
# print(' '.join(find_words))

