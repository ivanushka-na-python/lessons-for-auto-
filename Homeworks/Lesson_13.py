import os 
# print(os.path.dirname(__file__)) # узнаем абсолютный путь к открытой директории
base_path =(os.path.dirname(__file__)) # указываем путь до директории, не зависимо от расположения на компе
# file_path = f'{base_path}/Lesson_13.py'

# print(base_path)

file_path = os.path.join(base_path, 'some_file_with_text.txt') # расставялем слэши в зависимости от ос
new_file_path = os.path.join(base_path, 'test4.txt') # указываем путь до директории, в которой должен создстся файл по абсолютному пути 

# def file_read():
#    with open (file_path, 'r') as file:
#       for line in file.readlines():
#          yield(line) # yield не заканчивает работу после вывода одной строки как это делает return - return возвращает только один элемент(значение)
      
# for line in file_read():
#    with open (new_file_path, 'a') as new_file:
#       line = line.replace(',','')
#       new_file.write(line)      

# file_read()

test_folder_file_path = os.path.dirname(os.path.dirname(base_path)) # путь до более высокой в иерархии папке 
print(test_folder_file_path)


# with open ('') as test_folder_file:
#    print(test_folder_file)