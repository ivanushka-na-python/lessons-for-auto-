# распаковка - распределяем элементы коллекций по разным переменным (исп. только когда знаем точно количество элементов в коллекции)
my_list = [1, 2]
my_tuple = (1, 2, 3)
a, b = my_list
c, d, e = my_tuple
print (c, d, e)
print (a, b)

# # срез - достаем из коллекции опрделенную ее часть 
# list_1 = [2, 5.4, "text", 88, "number", 66, 98, 43]
# # print (list_1[0:4]) # от включительно - до не включительно
# # print (list_1[:4]) # если нужно сначала - можем не указывать в начале пордяковый номер элемента 
# # print (list_1[1:]) #если нужно до конца - можем не указывать в конце порядковый номер элемента

# # print (list_1[0::1]) # распечатываем через шаг (тут каждый второй элемент)
# # print (list_1[::-1]) # распечатываем все элементы с конца 
# # print (list_1[-1:-5:-1]) # распечатываем элементы с конца с -1 до -5 (не вкючительно)

# # методы строк, строка тоже похожа на коллекцию (последовательность символов - похожа на кортеж)
# text = "long1 long1 long3 long5 long1 long6 long7 long8 long9"
# # print (text[3]) 
# # print (len(text))
# # print (text.index("long5"))
# # print ("long0" in text)
# # print (text.count ("long1"))
# # print (text[:10])
# # print (text[10:])
# print (text[0:15:2])
# print (text.startswith("long2")) # начинается с какого-либо элемента
# print (text.endswith("long9")) # заканчивается каким-либо элементом

# some_text = "helLoW, HoW aRe yOU"
# # print (some_text.capitalize()) # делает первую букву заглавной 
# # print (some_text.title()) # делает кажду первую букву в слове заглавной 
# # print (some_text.upper()) # делает все буквы заглавыми 
# # print (some_text.lower()) # делает все буквы маленькими 

# word_index = some_text.lower().index("you")
# print (some_text[:word_index].lower() + some_text[word_index:].upper()) # делаем сначала весь текст маленьким, находим индекс нужного слова,
# # а после индекса нужного слова все пишем заглавными 


# перезаписывание строки на лету (не изменение)
# message = "Hello, world"
# message = message.replace("world", "friend") # replace отдает результат в начальную строку а сохраняет, чтобы к результату обратиться нужно этот результат 
# # присвоить изначальной переменной 
# print (message)

# some_text = " admin "
# some_text = some_text.replace (" ", "")
# print (some_text)

# # или можно взять функцию .strip - она чистит пробелы 
# some_text = some_text.strip() # чистим пробелы везде 
# some_text = some_text.lstrip() # чистим пробелы слева 
# some_text = some_text.rstrip() # чистим пробелы справа 
# print (some_text)

# text_with_extra_element = '"Hello"'
# text_with_extra_element = text_with_extra_element.strip('"') # убраем символы, которые указаны в скобках в единичных кавычках
# print (text_with_extra_element)

# # преобразования строки в список (коллекцию) и обратно 
# my_string = 'some text here'
# list_from_text = my_string.split() # разделение всех элементов 
# print (list_from_text)

# my_string2 = 'some,text,here'
# list_from_text2 = my_string2.split(',')
# print (list_from_text2)
# # преобразование строки в коллекцию позволяет работать с каждым элементом строки в отдельности 

# преобразование коллекции в строку 
# languages = ['first_lang', 'second_lang', 'third_lang']
# languages = ', '.join (languages) # сначала пишем "разделитель" и потом join
# print (languages)

# форматироавние строки 
# a = 'one'
# b = 'two'
# print ('First word is', a, ', second word is', b) # подставляем значение переменных в строку 

# # подсатвить значение можно еще через +, но так лучше нее делать 
# the_text = 'first word is ' + a + ' second word is ' + b
# print (the_text)

# string format приведены ниже (лучше использовать второй вариант)
# # лучше вставить значения переменных в строку через {} (опять не рекомендуемый формат оформления):
# my_text = 'first word is {}, second word is {}' # порядок вставляемых элементов должен идти в том порядке, в котором идут {} в строке
# print (my_text.format(a, b)) 

# a = 'one'
# b = 'two'
# my_text = 'first word is {0}, second word is {1}' # нужно пронумеровать номер под которым идет вствка из переменных {0} или {1} для этого примера, так же можно перегонять порядковые номера для вставки 
# print (my_text.format(a, b)) 

# # f-strig
# my_text = f'first word is {a}, second word is {b}'
# print (my_text)

# template = 'hello, {}!' # если нужнозаготовить шаблон заранее (типо получем данные после шаблона)
# username = input('What is your name?')
# print (template.format(username))

# username = input('What is your name?') # как по мне удобнее и проще так писать
# template = f'hello, {username}!'
# print (template)