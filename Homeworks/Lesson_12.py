# объектно ориентированное программирование 
# инкапсуляция - все данные объекта должны хранится в объекте, никто не может изменить данные объекта без его ведома...
# наследование - объекты и их классы организуют иерархию, дочерние классы наследуют свой функционал от материнских
# полиморфизм - способность классов менять свое поведение в зависисмости от типов опреаций и операндов, реализуются через перезагрузку метода/его переопределение

# файлы для работы должны находится в рабочей директории, там где есть директория .git

# import pathlib # узнаем абсолютный путь к открытому файлу, не использовать
# path_file = pathlib.Path('Lesson_12.py')
# print(pathlib)
 

import os 
print(os.path.dirname(__name__)) # узнаем абсолютный путь открытого файла, кажись напиздел
print(os.path.dirname(__file__)) # узнаем абсолютный путь к открытой директории
# print("Текущая рабочая директория:", os.getcwd()) # узнаем рабочую директорию 

# file_data = open('/Users/ivanusakov/Desktop/Projects/lessons-for-auto-/test.txt', 'r') # открываем файл по абсолютному пути 
# print(file_data)

# import json
# def read_file(file_name):
#    with open(file_name, 'r') as file: # открываем файл с указанием че будем делать w - запись, r - чтение, a - запись в конец
# # пользоваться данной функции для открытия и работы с файлом 
#       data = file.read() # читаем файл 
#       data = json.loads(data) # преобразование строки в объект питона, loads - превращение из строки в словарь, load - превращение всего файла в объект питона(словарь)
#       return(data)

# read_file('test2.txt') # вычитываеи и печатаем все содежимое файла 

# data_from_first_file = read_file('test2.txt')
# # data_from_first_file2 = read_file('test2.txt')

# print(data_from_first_file['temp'])

# import json
# class CountryData:
#       def __init__(self, file_name):
#            self.__name_file = file_name # ссылаемся с переменной file_name на имя файла 
#            self.__data = self.__read_some_data_file() # ссылаемся с переменной data на метод конвертации всего файла в словарь или в определенный мною класс
#            self.__country = self.__data['country']
#            self.__temp = self.__data['temp']
#            self.comfort = self.__comfort_temp()

#       def __read_some_data_file(self):
#           with open(self.__name_file, 'r') as file:
#                 return json.load(file)

#       def __comfort_temp(self):
#             return self.__temp >= 20
      
#       @property
#       def name_file(self):
#             return self.__name_file
#       @name_file.setter
#       def name_file(self, value):
#             self.__name_file = value
#       @property
#       def data(self):
#             return self.__data
#       @data.setter
#       def data(self, value):
#             self.__data = value
#       @property
#       def country(self):
#             return self.__country
#       @country.setter
#       def country(self, value):
#             self.__country = value
#       @property
#       def temp(self):
#             return self.temp
#       @temp.setter
#       def temp(self, value):
#             self.__temp = value

#       def __str__(self): # описал что должно отдаваться при попытке получить объект класса как строки(вместопросто его расположения на диске)
#             return f'{self.__name_file} with data {self.__data}'

#       def __repr__(self): 
#             return f'{self.__name_file} with data {self.__data}' # почему-то в каких-то случаях используется этот метод (типо надо сразу два реализовывать метода)

#       # def __lt__ (self, obj):
#       #    return self.temp < obj.temp
#                                        # хуйня какая-то 
#       # def __le__ (self, obj):
#       #    return self.temp <= obj.temp

#       def __add__ (self, obj):
#             return [self.data, obj.data]

# class MaxTemp(CountryData): # создаем дочерний класс для объекта, в котором больше данных
#       def __init__(self, file_name):
#             super().__init__(file_name)
#             self.__max_temp = self.data['max_temp'] # добавили переменную которая ссылается на доп данные из файла
#       @property
#       def max_temp(self):
#             return self.__max_temp
#       @max_temp.setter
#       def max_temp(self, value):
#             self.__max_temp = value

# country_russia = CountryData('Country_statics.txt')
# country_turkey2 = CountryData('test2.txt')
# country_turkey3 = MaxTemp('test3.txt')

# print(country_russia.country)
# print(country_russia.comfort)
# print(country_turkey3.max_temp)
# print(country_russia.Country)
# print(country_russia.__data)
# print(country_turkey2.Country)
# print(country_turkey2.data)
# print(country_turkey3.max_temp)
# print(country_turkey3.__comfort)

# # # блять, надо разобраться с приватными именами переменных и методами в классах согласно инкапсуляции
# # # хуйня какая-то, потому что при подстановке __ к переменным доступ к ним не осуществляется 

# print(country_russia)
# # print(country_russia <= country_turkey2)
# print(country_russia + country_turkey2)